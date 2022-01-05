from brain_games.games.answer_checker import check_answer
import operator
import prompt
import random


def calc_game(username: str):
    def calc_logic():
        # Inputs to next two randint functions are arbitrary.
        question_num1 = random.randint(1, 101)
        question_num2 = random.randint(1, 101)
        question_signs = ['+', '-', '*']
        operator_functions = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }
        random_operation_sign = random.choice(question_signs)
        question = "{0} {1} {2}".format(question_num1, random_operation_sign, question_num2)
        return operator_functions[random_operation_sign](question_num1, question_num2),\
            'Question: {0}'.format(question)
    correct_answer_count = 0
    print("What is the result of the expression? ")
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
        correct_answer, question = calc_logic()
        print(question)
        user_answer = prompt.string("Your answer: ")
        if check_answer(user_answer=user_answer,
                        correct_answer=str(correct_answer),
                        username=username):
            correct_answer_count += 1
        else:
            break
