from random import randint


def check_even(position):
    if position % 2 == 0:
        return "yes"
    else:
        return "no"


def calculate(position1, position2, sign):
    if sign == " - ":
        return position1 - position2
    elif sign == " + ":
        return position1 + position2
    elif sign == " * ":
        return position1 * position2
    else:
        return "no"


def check_gcd(num1, num2):
    num = min(num1, num2)
    for i in range(num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


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


if __name__ == "__main__":
    prg_check()
