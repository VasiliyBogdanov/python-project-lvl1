"""Engine for brain_games."""

import prompt

GAME_QUESTIONS = {
    "brain_calc": "What is the result of the expression?",
    "brain_even": 'Answer "yes" if the number is even, otherwise answer "no".',
    "brain_gcd": 'Find the greatest common divisor of given numbers.',
    "brain_prime": 'Answer "yes" if given number is prime. '
                   'Otherwise answer "no".',
    "brain_progression": "What number is missing in the progression?"
}


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


def engine(game_name: str, username: str, game_logic):
    """Execute game logic.
    game_logic needs to be a function, that returns a tuple with
        correct answer and question for particular game:
            (correct_answer, question)
    """
    correct_answer_count = 0
    print(GAME_QUESTIONS[game_name])
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
        correct_answer, question = game_logic()
        print(question)
        user_answer = prompt.string("Your answer: ")
        if check_answer(user_answer=user_answer,
                        correct_answer=str(correct_answer),
                        username=username):
            correct_answer_count += 1
        else:
            break
