from brain_games.calculator import prime_check
from brain_games.answers import answer
import prompt


def check_answer(name='Bill'):
    count = 3
    while count != 0:
        number, prime = prime_check()
        guess = prompt.string('Answer "yes" if the number is prime, '
                              'otherwise answer "no".\n'
                              f'Question: {number}\n'
                              'Your answer: ')
        count = answer(guess, prime, count, name)
        if count == 3:
            break
    if count == 0:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    check_answer()
