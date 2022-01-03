import prompt


def welcome():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def check_answer(user_answer, correct_answer, username: str):
    """Check answer for games functions."""
    if user_answer == correct_answer:
        print('Correct!')
        return True
    elif user_answer != correct_answer:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, correct_answer))
        print("Let's try again, {0}!".format(username))
        return False
