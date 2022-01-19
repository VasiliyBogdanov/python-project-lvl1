import prompt
from typing import Callable

QUESTION = "Question: "
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


def welcome_user() -> None:
    print(MESSAGES["welcome"])


def get_username() -> str:
    username = prompt.string(MESSAGES["ask_name"])
    return username


def greet_user(username) -> None:
    print(MESSAGES["greetings"].format(username))


def welcome_to_brain_games() -> None:
    welcome_user()
    greet_user(get_username())


def engine(game_question: str,
           game_logic: Callable[[], tuple[str, str]]) -> None:
    welcome_user()
    username = get_username()
    greet_user(username)
    correct_answer_count = 0
    print(game_question)
    while correct_answer_count < NUMBER_OF_ROUNDS:
        correct_answer, question = game_logic()
        print(question)
        user_answer = prompt.string(MESSAGES["your_answer"])
        if user_answer.lower() == correct_answer.lower():
            print(MESSAGES["correct"])
            correct_answer_count += 1
        else:
            print(MESSAGES["wrong"].format(user_answer, correct_answer))
            print(MESSAGES["try_again"].format(username))
            break
    else:
        print(MESSAGES["congratulations"].format(username))
