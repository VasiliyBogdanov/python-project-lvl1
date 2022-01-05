from brain_games.answer_checker import check_answer
import prompt
import random


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
        answer = progression[question_position]
        progression[question_position] = ".."
        output_question = "Question: "
        for i in progression:
            output_question += str(i) + " "
        return answer, output_question

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
