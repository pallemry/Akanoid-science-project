from tkinter import *
from data import *
from question import rev
from typing import Callable, Sequence
import question, utils, random, time
root = Tk()
root.title("משחק העששת הבינלאומי")
root.geometry("500x570")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="white")
canvas.pack(padx=10, pady=10)
score = Label(height=50, width=80, text="ניקוד: 0", font="Arial 14 bold")
score.pack(side="left")

class Bricks:
    def __init__(self, canvas, color, fact: question.question_info = None):
        self.fact = fact
        self.isFact = fact is not None
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_oval(5, 5, 25, 25, fill=color, width=2)

root.update()

class Ball:
    def __init__(self, canvas, color, paddle, bricks, score):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.bottom_hit = False
        self.hit = 0
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color, width=1)
        self.canvas.move(self.id, 230, 461)
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
       
        self.x = start[0]
        self.y = -start[0]
        self.canvas.move(self.id, self.x, self.y)
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

    def brick_hit(self, pos) -> tuple[bool, Bricks]:
        for brick_line in self.bricks:
            for brick in brick_line:
                brick_pos = self.canvas.coords(brick.id)
              
                try:
                    if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                        if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                            canvas.bell()
                            self.hit += 1
                            self.score.configure(text="ניקוד: " + str(self.hit))
                            self.canvas.delete(brick.id)
                            return (True, brick)
                except:
                    continue
        return (False, None)
    
        
    def paddle_hit(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
               
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
    
        start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
        random.shuffle(start)
        a: Bricks = None
        is_hit = self.brick_hit(pos)
        if is_hit[0]:
            self.y = start[0]
            a = is_hit[1]
        if pos[1] <= 0:
            self.y = start[0]
        if pos[3] >= self.canvas_height:
            self.bottom_hit = True
        if pos[0] <= 0:
            self.x = start[0]
        if pos[2] >= self.canvas_width:
            self.x = -start[0]
        if self.paddle_hit(pos):
            self.y = -start[0]
        return a

        
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 485)
        self.x = 0
        self.pausec=0
        self.byForce = False
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all("<Left>", self.turn_left)
        self.canvas.bind_all("<Right>", self.turn_right)
        self.canvas.bind_all("<space>", self.pauser)
        

    def draw(self):
        pos = self.canvas.coords(self.id)
        
        if pos[0] + self.x <= 0:
            self.x = 0
        if pos[2] + self.x >= self.canvas_width:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

    def turn_left(self, event):
        self.x = -3.5

    def turn_right(self, event):
        self.x = 3.5

    def pauser(self,event=None,byForce=False):
        self.byForce = byForce
        self.pausec+=1
        if self.pausec>=2 and not byForce:
            self.byForce = False
            self.pausec=0
    




playing = False

qs: Sequence[question.question_info] = utils.clone_question_array(questions)
# playing = True
def start_game(event):
    global playing, qs
    if playing is False or len(qs) == 0:
        playing = True
        score.configure(text="ניקוד: 0")
        canvas.delete("all")
        BALL_COLOR = ["black"]
        BRICK_COLOR = "White"
        SPECIAL_BRICK_COLOR = "RED"
        random.shuffle(BALL_COLOR)
        paddle = Paddle(canvas, "Dark Blue")
        bricks = []
        fact_count = 0
        for i in range(0, 2):
            b = []
            for j in range(0, 19):
                if fact_count < len(questions):
                    current_question = questions[fact_count]
                    print(current_question)
                    tmp = Bricks(canvas, SPECIAL_BRICK_COLOR, utils.clone_question(current_question))
                else:
                    tmp = Bricks(canvas, BRICK_COLOR)
                fact_count += 1
                b.append(tmp)
            bricks.append(b)
        utils.shuffle2d(bricks)
        for i in range(0, 2):
            for j in range(0, 19):
                canvas.move(bricks[i][j].id, 25 * j, 25 * i)

        ball = Ball(canvas, BALL_COLOR[0], paddle, bricks, score)
        root.update_idletasks()
        root.update()
        temp_fact = "עובדה מעניינת לי את התחת"
        time.sleep(1)
        qs = []
        while 1:
            if paddle.pausec != 1:
                try:
                    canvas.delete(m)
                    del m
                except:
                    pass
                if not ball.bottom_hit:
                    brick = ball.draw()
                    paddle.draw()
                    root.update_idletasks()
                    root.update()
                    if brick is not None:
                        if brick.isFact == True:
                            temp_fact = brick.fact
                            qs.append(utils.clone_question(brick.fact))
                            paddle.pauser(None,True)
                            pass
                    time.sleep(0.01)
                    if ball.hit==95:
                        canvas.create_text(250, 250, text=rev("ניצחת"), fill="yellow", font="Consolas 24 ")
                        root.update_idletasks()
                        root.update()
                        playing = False
                        break
                else:
                    s = ["אכזבה + כשלון", "המשחק הסתיים", "נו מה אתה פרה?", "תשתפר כבר"]
                    word = rev(s[random.Random().randint(0, len(s) - 1)])
                    canvas.create_text(250, 250, text=word, fill="red", font="Consolas 24 ")
                    root.update_idletasks()
                    root.update()
                    playing = True
                    try:
                        m
                        canvas.delete(m)
                    except UnboundLocalError:
                        print("??")
                    break
            else:
                try:
                    if m==None:pass
                except:
                    
                    s = "נעצר"
                    if paddle.byForce:
                        s = temp_fact.fact

                    m=canvas.create_text(250, 250, text=rev(s), fill="green", font="Consolas 12 ")
                root.update_idletasks()
                root.update()
    else:
        canvas.delete("all")

        #!# This is for testing
        # qs = []

        # for i in range(2):
        #     answers = ["לא", "לא", "לא", "כן"]
        #     random.shuffle(answers)
        #     correct_num = answers.index("כן")
        #     qs.append(question.question_info("מחלת העששת הומצאה ב", answers, correct_num, lambda x: print(x)))
        #!# end

        score.configure(text='ניקוד: 0')
        q = question.question(canvas, root, qs, score)
        q.start()
        playing = False

root.bind_all("<Return>", start_game)
canvas.create_text(250, 250, text="תתחיל " + rev("למה אתה מחכה?"), fill="Black", font="Consolas 18")
j=canvas.find_all()
root.mainloop()