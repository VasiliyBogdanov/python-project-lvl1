import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))
    return username


def check_answer(user_answer: str, correct_answer: str, username: str):
    if user_answer.lower() == correct_answer.lower():
        print('Correct!')
        return True
    else:
        print("'{0}' is wrong answer ;(. "
              "Correct answer was '{1}'.".format(user_answer, correct_answer))
        print("Let's try again, {0}!".format(username))
        return False


def engine(game_question: str, game_logic):
    username = welcome_user()
    correct_answer_count = 0
    print(game_question)
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
