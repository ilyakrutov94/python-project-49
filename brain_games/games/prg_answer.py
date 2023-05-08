from brain_games.calculator import prg_check
from brain_games.answers import answer
import prompt


def check_answer(name='Bill'):
    count = 3
    while count != 0:
        missing_number, string_of_numbers = prg_check()
        guess = prompt.string('What number is missing in the progression?\n'
                              f'Question: {string_of_numbers}\n'
                              'Your answer: ')
        count = answer(guess, missing_number, count, name)
    print(f"Congratulations, {name}")


if __name__ == "__main__":
    check_answer()
