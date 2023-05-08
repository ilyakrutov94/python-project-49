from random import randint
from brain_games.calculator import check_gcd
import prompt


def check_answer(name):
    count = 3
    while count != 0:
        number1 = randint(1, 50)
        number2 = randint(1, 50)
        string1 = str(number1) + ' ' + str(number2)
        guess = prompt.string('Find the greatest common divisor '
                              'of given numbers.\n'
                              f'Question: {string1}\n'
                              'Your answer: ')
        if int(guess) == check_gcd(number1, number2):
            count -= 1
            print("Correct!")
        else:
            print(f"'{guess}'is wrong answer;(. Correct answer "
                  "was '{calculate(number1, number2, sign)}'.\n"
                  f"Let's try again, {name}!")
            count = 3
    print(f"Congratulations, {name}")


if __name__ == "__main__":
    check_answer('Bill')
