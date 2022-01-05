def check_answer(user_answer: str, correct_answer: str, username: str):
    """Check answer for games functions."""
    if user_answer.lower() == correct_answer.lower():
        print('Correct!')
        return True
    elif user_answer.lower() != correct_answer.lower():
        print("'{0}' is wrong answer ;(. "
              "Correct answer was '{1}'.".format(user_answer, correct_answer))
        print("Let's try again, {0}!".format(username))
        return False