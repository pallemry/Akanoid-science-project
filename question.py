import random
from tkinter import *
from typing import *
import time

def rev(s: str) -> str:
    questionM = False
    if '?' in s:
        questionM = True
        s=s.replace("?", "")
    w = s.split(' ')
    w.reverse()
    return ('?' if questionM else "") + " ".join(w)

def maptoalpha(i: int) -> str:
    if i == 0: return "א"
    if i == 1: return "ב"
    if i == 2: return "ג"
    if i == 3: return "ד"
    if i == 4: return "ה"
    return str(i)

class question_info:
    nextType = Callable[[bool], None]
    def __init__(self, question: str, answers: list[str], correct_num: int, next: nextType, fact: str):
        self.fact = fact
        self.question = question
        self.answers = answers
        self.correct_num = correct_num
        self.actions: list[Callable] = []
        self.updateNext(next)
    
    def updateNext(self, next: nextType):
        self.actions = []
        for i in range(len(self.answers)):
            self.actions.append(question_info.createAction(next, i == self.correct_num))

    def createAction(next: nextType, isCorrect: bool = False) -> Callable:
        def x(e):
            next(isCorrect)
        return x
    
    def shuffle_answers(self):
        correct_answer = self.answers[self.correct_num]
        random.shuffle(self.answers)
        self.correct_num = self.answers.index(correct_answer)


class question:
    def __init__(self,canvas: Canvas, root: Tk, question: Sequence[question_info], scoreLable: Label) -> None:
        self.canvas = canvas
        self.root = root
        self.scoreNum = 0
        self.scoreLable = scoreLable
        self.num = -1
        self.questions = question
        return
        
    def advance(self):
        self.num +=1
        if self.num >= len(self.questions):
            # The quiz is over!
            return
        def on_next(isCorrect: bool):
            self.canvas.delete("all")
            if isCorrect:
                self.scoreNum+=1
                self.scoreLable.configure(text='ניקוד: ' + str(self.scoreNum))
            self.canvas.create_text(250, 250, text= "!" + rev("התשובה נכונה" if isCorrect else "התשובה לא נכונה"), fill=("green" if isCorrect else "red"), font="Consolas 24 ")
            self.root.update_idletasks()
            self.root.update()
            time.sleep(1)
            self.advance()
            return
        q = self.questions[self.num]
        q.shuffle_answers()
        q.updateNext(on_next)
        self.canvas.delete("all")
        self.canvas.create_text(250, 250, text=rev(q.question), fill="red", font="Consolas 15 ")
        self.possible_answers: list[str] = []
        for i in range(len(q.answers)):
            possible_answer = q.answers[i]
            o = self.canvas.create_text(250, 250 + 30 * (i + 1), text=rev(maptoalpha(i) + " " + possible_answer), fill="red", font="Consolas 15")
            self.canvas.tag_bind(o, "<Button-1>", q.actions[i])
            self.possible_answers.append(o)
        self.root.update_idletasks()
        self.root.update()
    def start(self):
        self.canvas.delete("all")
        self.advance()
    
    

    def run(self):
        # def dosome():
        #     print(1)
        # if self.num == 1:
        #     self.canvas.create_text(250, 250, text=("שאלה 1"), fill="red", font="Consolas 24 ")
        #     self.o1 = self.canvas.create_text(250, 300, text=("א"), fill="black", font="Consolas 24 ")
        #     self.o2 = self.canvas.create_text(250, 350, text=("ב"), fill="black", font="Consolas 24 ")
        #     self.o3 = self.canvas.create_text(250, 400, text=("ג"), fill="black", font="Consolas 24 ")
        #     self.canvas.tag_bind(self.o1, dosome)
        return
