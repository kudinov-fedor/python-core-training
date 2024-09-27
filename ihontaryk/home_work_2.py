""" Functions for Home work 2"""


def fizz_buzz(number):
    """fizz_buzz function"""
    if type(number) is not int:
        raise TypeError
    if number == 0:
        raise ValueError
    if number % 15 == 0:
        result = "FizzBuzz"
    elif number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result = "Buzz"
    else:
        result = str(number)

    return result


def multiply_numbers(number1, number2):
    """multiply_numbers function"""
    if (type(number1) and type(number2)) in (int or float):
        return number1 * number2
    else:
        raise TypeError


def sum_numbers(text):
    """sum_numbers function"""
    total = 0

    words = text.split(" ")
    for word in words:
        if word.isdecimal():
            total += int(word)

    return total
