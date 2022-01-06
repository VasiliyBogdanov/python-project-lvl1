import random

MIN_QUESTION_NUMBER = 1
MAX_QUESTION_NUMBER = 101


def is_prime(n):
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 1 / 2) + 1):
        if n % i == 0:
            return False
    return True


def prime_logic():
    question_integer = random.randint(MIN_QUESTION_NUMBER, MAX_QUESTION_NUMBER)
    correct_answer = 'yes' if is_prime(question_integer) else 'no'
    question = "Question: {0}".format(question_integer)
    return correct_answer, question
