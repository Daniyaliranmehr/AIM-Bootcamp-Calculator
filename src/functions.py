def add(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2

def percentage(num, percent):
    return num * percent / 100
def power(base, exponent):
    if base == 0 and exponent < 0:
        return "Error! Zero cannot be raised to a negative power."
    return base ** exponent


def factorial(num):
    if type(num) != int or num < 0:
        return "Error! Factorial requires a non-negative integer."

    result = 1

    for i in range(1, num + 1):
        result *= i

    return result
