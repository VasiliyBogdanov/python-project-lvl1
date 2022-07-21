import operator
import random

from brain_games.engine import engine, QUESTION

GAME_QUESTION = "What is the result of the expression?"
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101
QUESTION_ARGUMENTS = "{0} {1} {2}"


def calc_logic() -> (str, str):
    question_num1 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    question_num2 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    question_signs = ['+', '-', '*']
    operator_functions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    random_operation_sign = random.choice(question_signs)
    correct_answer = operator_functions[random_operation_sign](question_num1,
                                                               question_num2)
    question = QUESTION + QUESTION_ARGUMENTS \
        .format(question_num1, random_operation_sign, question_num2)
    return str(correct_answer), question


def calc_game() -> None:
    engine(game_question=GAME_QUESTION,
           game_logic=calc_logic)
