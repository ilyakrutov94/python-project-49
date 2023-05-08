from brain_games.calculator import calculate
from brain_games.answers import answer
import prompt


def check_answer(name='Bill'):
    count = 3
    while count != 0:
        question_string, equation = calculate()
        guess = int(prompt.string('What is the result of the expression?\n'
                                  f'Question: {question_string}\n'
                                  'Your answer: '))
        count = answer(guess, equation, count, name)
        if count == 3:
            break
    if count == 0:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    check_answer()
