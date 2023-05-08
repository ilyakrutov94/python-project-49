from brain_games.calculator import prg_check
import prompt


def check_answer(name='Bill'):
    count = 3
    while count != 0:
        missing_number, string_of_numbers = prg_check()
        guess = prompt.string('What number is missing in the progression?\n'
                              f'Question: {string_of_numbers}\n'
                              'Your answer: ')
        if guess == missing_number:
            count -= 1
            print("Correct!")
        else:
            print(f"'{guess}'is wrong answer;(. Correct answer "
                  f"was '{missing_number}'.\n"
                  f"Let's try again, {name}!")
            count = 3
    print(f"Congratulations, {name}")


if __name__ == "__main__":
    check_answer()
