import random

GAME_NAME = 'brain_even'
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101


def even_logic():
    question_integer = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = 'yes' if question_integer % 2 == 0 else 'no'
    question = 'Question: {0}'.format(question_integer)
    return correct_answer, question
