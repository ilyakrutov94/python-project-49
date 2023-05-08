from brain_games.calculator import check_even
from brain_games.answers import answer
import prompt


def check_answer(name='Bill'):
    count = 3
    while count != 0:
        question, equation = check_even()
        guess = prompt.string('Answer "yes" if the number is even, '
                              'otherwise answer "no".\n'
                              f'Question: {question}\n'
                              'Your answer: ')
        count = answer(guess, equation, count, name)
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    check_answer()
