"""
***** Task2 *****
You should write a function that will receive a positive integer and return: "Fizz" if the number is divisible
by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").
"""


def checkio(num: int) -> str:
    if num % 3 == 0:
        res = 'Fizz'
    else:
        res = str(num)
    return res
