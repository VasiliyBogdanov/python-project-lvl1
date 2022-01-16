import prompt
from typing import Callable

NUMBER_OF_ROUNDS = 3
MESSAGES = {
    "welcome": 'Welcome to the Brain Games!',
    "ask_name": 'May I have your name? ',
    "greetings": 'Hello, {0}!',
    "correct": 'Correct!',
    "wrong": "'{0}' is wrong answer ;(. "
             "Correct answer was '{1}'.",
    "try_again": "Let's try again, {0}!",
    "your_answer": "Your answer: ",
    "congratulations": 'Congratulations, {0}!'
}


def welcome_user() -> str:
    print(MESSAGES["welcome"])
    username = prompt.string(MESSAGES["ask_name"])
    print(MESSAGES["greetings"].format(username))
    return username


def check_answer(user_answer: str, correct_answer: str, username: str) -> bool:
    if user_answer.lower() == correct_answer.lower():
        print(MESSAGES["correct"])
        return True
    else:
        print(MESSAGES["wrong"].format(user_answer, correct_answer))
        print(MESSAGES["try_again"].format(username))
        return False


def engine(game_question: str, game_logic: Callable[[], tuple[str, str]]) -> None:
    username = welcome_user()
    correct_answer_count = 0
    print(game_question)
    while correct_answer_count < NUMBER_OF_ROUNDS:
        correct_answer, question = game_logic()
        print(question)
        user_answer = prompt.string(MESSAGES["your_answer"])
        if check_answer(user_answer=user_answer,
                        correct_answer=correct_answer,
                        username=username):
            correct_answer_count += 1
        else:
            break
    else:
        print(MESSAGES["congratulations"].format(username))