#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import check_answer, welcome, welcome_user


def progression_game(username: str):
    def make_question():
        """Return tuple with correct answer and formatted question.
            (
            progression[question_position]: int,
            output_question: str
            )
        """
        first_num = random.randint(1, 101)
        prog_length = random.randint(5, 10)
        prog_step = random.randint(2, 9)
        progression = [i * prog_step + first_num for i in range(prog_length)]
        question_position = random.randint(0, len(progression) - 1)
        output_question = "Question: "
        for i in progression:
            output_question += str(i) + " "
        output_question = output_question.replace(str(progression[question_position]), "..")
        return progression[question_position], output_question

    correct_answer_count = 0
    print("What number is missing in the progression?")
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
        correct_answer, question = make_question()
        print(question)
        user_answer = prompt.string("Your answer: ")
        if check_answer(user_answer=user_answer,
                        correct_answer=str(correct_answer),
                        username=username):
            correct_answer_count += 1
        else:
            break


def main():
    welcome()
    username = welcome_user()
    progression_game(username)


if __name__ == '__main__':
    main()
