import math
import random
from brain_games.engine import engine, QUESTION

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101
QUESTION_ARGUMENTS = "{0} {1}"


def gcd_logic() -> (str, str):
    question_num1 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    question_num2 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = math.gcd(question_num1, question_num2)
    question = QUESTION + QUESTION_ARGUMENTS\
        .format(question_num1, question_num2)
    return str(correct_answer), question


def gcd_game() -> None:
    engine(game_question=GAME_QUESTION,
           game_logic=gcd_logic)
