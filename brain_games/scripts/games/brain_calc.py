#!/usr/bin/env python3
import prompt
import operator
import random
from brain_games.cli import check_answer, welcome, welcome_user


def calc_game(username: str):
    correct_answer_count = 0
    print("What is the result of the expression? ")
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
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
        print('Question: {0}'.format(question))
        user_answer = prompt.string("Your answer: ")
        correct_answer = operator_functions[random_operation_sign](question_num1, question_num2)
        if check_answer(user_answer=user_answer,
                        correct_answer=str(correct_answer),
                        username=username):
            correct_answer_count += 1
        else:
            break


def main():
    welcome()
    username = welcome_user()
    calc_game(username)


if __name__ == '__main__':
    main()
