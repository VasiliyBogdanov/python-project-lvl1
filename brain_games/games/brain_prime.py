from brain_games.cli import check_answer
import prompt
import random


def prime_game(username: str):
    def is_prime(n):
        """Return True if n is prime number."""
        if n <= 1:
            return False
        for i in range(2, int(n ** 1 / 2) + 1):
            if n % i == 0:
                return False
        return True
    correct_answer_count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while True:
        if correct_answer_count >= 3:
            print('Congratulations, {0}!'.format(username))
            break
        # Input to next randint function is arbitrary.
        question = random.randint(1, 100)
        print("Question: {0}".format(question))
        correct_answer = 'yes' if is_prime(question) else 'no'
        user_answer = prompt.string("Your answer: ")
        if check_answer(user_answer=user_answer,
                        correct_answer=str(correct_answer),
                        username=username):
            correct_answer_count += 1
        else:
            break
