#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.brain_games import welcome, welcome_user


def numbers_game(username: str):
    """Execute main logic."""
    correct_answer_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
        question = random.randint(1, 100)
        correct_answer = 'yes' if question % 2 == 0 else 'no'
        print('Question: {0}'.format(question))
        user_answer = prompt.string("Your answer: ")
        if user_answer.lower() == correct_answer.lower():
            print('Correct!')
            correct_answer_count += 1
        elif user_answer.lower() != correct_answer.lower():
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, correct_answer))
            print("Let's try again, {0}!".format(username))
            break


def main():
    """Execute main logic."""
    welcome()
    username = welcome_user()
    numbers_game(username)


if __name__ == '__main__':
    main()
