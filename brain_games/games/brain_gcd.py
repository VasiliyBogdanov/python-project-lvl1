import math
import random

GAME_NAME = 'brain_gcd'
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101


def gcd_logic():
    question_num1 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    question_num2 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = math.gcd(question_num1, question_num2)
    question = "Question: {0} {1}".format(question_num1, question_num2)
    return correct_answer, question
