import random, question
from typing import Sequence

def shuffle2d(array: list[list]):
    for i in range(len(array)):
        sub_array = array[i]
        for k in range(len(sub_array)):
            row = random.randint(0, len(array) - 1)
            col = random.randint(0, len(sub_array) - 1)
            item = array[i][k]
            tmp = array[row][col]
            array[i][k] = tmp
            array[row][col] = item

def clone_array(array: list):
    x = []
    for item in array:
        x.append(item)
    return x

def clone_question(q: question.question_info) -> question.question_info:
    def fn(x):
        return
    fact = q.fact
    questionstr = q.question
    corr = q.correct_num
    nextfn = fn
    answers = clone_array(q.answers)
    return question.question_info(questionstr, answers, corr, nextfn, fact)

def clone_question_array(q: Sequence[question.question_info]) -> Sequence[question.question_info]:
    x = []
    for qx in q:
        x.append(clone_question(qx))
    return x