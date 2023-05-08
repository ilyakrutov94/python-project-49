def answer(guess, equation, count, name):
    if guess == equation:
        count -= 1
        print("Correct!")
        return count
    else:
        print(f"'{guess}'is wrong answer;(. Correct answer "
              f"was '{equation}'.\n"
              f"Let's try again, {name}!")
        count = 3
        return count
