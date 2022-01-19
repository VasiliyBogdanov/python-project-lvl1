import random
from brain_games.engine import engine, QUESTION

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101
QUESTION_ARGUMENTS = '{0}'
ANSWER = {
    "yes": 'yes',
    "no": 'no'
}


def even_logic() -> (str, str):
    question_integer = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = ANSWER["yes"] if question_integer % 2 == 0 \
        else ANSWER["no"]
    question = QUESTION + QUESTION_ARGUMENTS.format(question_integer)
    return correct_answer, question


def even_game() -> None:
    engine(game_question=GAME_QUESTION,
           game_logic=even_logic)
