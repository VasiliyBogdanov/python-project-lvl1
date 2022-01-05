from brain_games.answer_checker import check_answer
import prompt
import random


def numbers_game(username: str):
    correct_answer_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
        # Inputs to next randint function is arbitrary.
        question = random.randint(1, 100)
        correct_answer = 'yes' if question % 2 == 0 else 'no'
        print('Question: {0}'.format(question))
        user_answer = prompt.string("Your answer: ")
        if check_answer(user_answer=user_answer,
                        correct_answer=correct_answer,
                        username=username):
            correct_answer_count += 1
        else:
            break
