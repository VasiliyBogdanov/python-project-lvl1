import math
import random

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101
QUESTION = "Question: {0} {1}"


def gcd_logic() -> (str, str):
    question_num1 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    question_num2 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = math.gcd(question_num1, question_num2)
    question = QUESTION.format(question_num1, question_num2)
    return str(correct_answer), question
