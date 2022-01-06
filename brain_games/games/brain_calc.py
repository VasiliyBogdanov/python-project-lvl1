import operator
import random

MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101


def calc_logic():
    question_num1 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    question_num2 = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    question_signs = ['+', '-', '*']
    operator_functions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    random_operation_sign = random.choice(question_signs)
    correct_answer = operator_functions[random_operation_sign](question_num1,
                                                               question_num2)
    question = "Question: {0} {1} {2}" \
        .format(question_num1, random_operation_sign, question_num2)
    return correct_answer, question
