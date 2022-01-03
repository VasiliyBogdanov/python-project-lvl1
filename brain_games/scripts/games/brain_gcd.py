#!/usr/bin/env python3
import math
import prompt
import random
from brain_games.cli import check_answer, welcome, welcome_user


def gcd_game(username):
    correct_answer_count = 0
    print('Find the greatest common divisor of given numbers.')
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
        question_num1 = random.randint(1, 101)
        question_num2 = random.randint(1, 101)
        question = "{0} {1}".format(question_num1, question_num2)
        print("Question: {0}".format(question))
        user_answer = prompt.string("Your answer: ")
        correct_answer = math.gcd(question_num1, question_num2)
        if check_answer(user_answer=user_answer,
                        correct_answer=str(correct_answer),
                        username=username):
            correct_answer_count += 1
        else:
            break


def main():
    welcome()
    username = welcome_user()
    gcd_game(username)


if __name__ == '__main__':
    main()