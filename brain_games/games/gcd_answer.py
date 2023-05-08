from brain_games.calculator import check_gcd
from brain_games.answers import answer
import prompt


def check_answer(name='Bill'):
    count = 3
    while count != 0:
        pair_of_numbers, equation = check_gcd()
        guess = int(prompt.string('Find the greatest common divisor '
                                  'of given numbers.\n'
                                  f'Question: {pair_of_numbers}\n'
                                  'Your answer: '))
        count = answer(guess, equation, count, name)
    print(f"Congratulations, {name}")


if __name__ == "__main__":
    check_answer()
