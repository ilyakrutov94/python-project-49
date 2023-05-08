from random import randint, choice
from brain_games.calculator import calculate
import prompt
list_of_signs = [" + ", " - ", " * "]


def check_answer(name):
    count = 3
    while count != 0:
        number1 = randint(1, 3)
        number2 = randint(1, 3)
        sign = choice(list_of_signs)
        string1 = str(number1) + str(sign) + str(number2)
        guess = prompt.string('What is the result of the expression?\n'
                              f'Question: {string1}\n'
                              'Your answer: ')
        if int(guess) == calculate(number1, number2, sign):
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
