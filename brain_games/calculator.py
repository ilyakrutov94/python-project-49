from random import randint, choice


def check_even():
    number = randint(1, 100)
    if number % 2 == 0:
        answer = 'yes'
        return (number, answer)
    else:
        answer = 'no'
        return (number, answer)


def calculate():
    list_of_signs = [" + ", " - ", " * "]
    number1 = randint(1, 3)
    number2 = randint(1, 3)
    sign = choice(list_of_signs)
    question_string = str(number1) + str(sign) + str(number2)
    if sign == " - ":
        equation = number1 - number2
        return (question_string, equation)
    elif sign == " + ":
        equation = number1 + number2
        return (question_string, equation)
    elif sign == " * ":
        equation = number1 * number2
        return (question_string, equation)


def check_gcd():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    pair_of_numbers = str(number1) + ' ' + str(number2)
    min_num = min(number1, number2)
    for i in range(min_num, 0, -1):
        if number1 % i == 0 and number2 % i == 0:
            return (pair_of_numbers, i)


def prg_check():
    start = randint(2, 4)
    itera = randint(2, 4)
    leng = randint(5, 10)
    stop = start + itera*leng
    list1 = [str(i) for i in range(start, stop, itera)]
    position = randint(0, len(list1)-1)
    number = list1[position]
    list1[position] = '..'
    list_new = ' '.join(list1)
    return (number, list_new)


def prime_check():
    number = randint(1, 100)
    dividers = 0
    for i in range(2, number // 2+1):
        if number % i == 0:
            dividers += 1
    if dividers <= 0:
        answer = 'yes'
        return (number, answer)
    else:
        answer = 'no'
        return (number, answer)


if __name__ == "__main__":
    prime_check()
