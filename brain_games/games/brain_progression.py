import random

MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
MIN_PROGRESSION_STEP = 5
MAX_PROGRESSION_STEP = 10


def progression_logic():
    first_num = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    prog_length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    prog_step = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    progression = [i * prog_step + first_num for i in range(prog_length)]
    question_position = random.randint(0, len(progression) - 1)
    correct_answer = progression[question_position]
    progression[question_position] = ".."
    question = "Question: "
    for i in progression:
        question += str(i) + " "
    return correct_answer, question
