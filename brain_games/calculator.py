def check_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def calculate(number1, number2, sign):
    if sign == " - ":
        return number1 - number2
    elif sign == " + ":
        return number1 + number2
    elif sign == " * ":
        return number1 * number2
    else:
        return "no"


def check_gcd(num1, num2):
    num = min(num1, num2)
    for i in range(num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
