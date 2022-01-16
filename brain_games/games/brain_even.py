import random

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101
QUESTION = 'Question: {0}'
ANSWER = {
    "yes": 'yes',
    "no": 'no'
}


def even_logic() -> (str, str):
    question_integer = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = ANSWER["yes"] if question_integer % 2 == 0 \
        else ANSWER["no"]
    question = QUESTION.format(question_integer)
    return correct_answer, question
