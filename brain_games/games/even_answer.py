from random import randint
from brain_games.calculator import check_even
import prompt


def check_answer(name):
    count = 3
    while count != 0:
        number = randint(1, 100)
        guess = prompt.string('Answer "yes" if the number is even, '
                              'otherwise answer "no".\n'
                              f'Question: {number}\n'
                              'Your answer: ')
        if guess == check_even(number):
            count -= 1
            print("Correct!")
        else:
            print("'yes is wrong answer;(. Correct answer was 'no'.\n"
                  f"Let's try again, {name}!")
            count = 3
    print(f"Congratulations, {name}")


if __name__ == "__main__":
    check_answer('Bill')
