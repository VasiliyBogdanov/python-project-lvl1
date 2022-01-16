import random

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101
QUESTION = "Question: {0}"
ANSWER = {
    "yes": 'yes',
    "no": 'no'
}


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 1 / 2) + 1):
        if n % i == 0:
            return False
    return True


def prime_logic() -> (str, str):
    question_integer = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = ANSWER["yes"] if is_prime(question_integer) \
        else ANSWER["no"]
    question = QUESTION.format(question_integer)
    return correct_answer, question
