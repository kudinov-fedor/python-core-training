"""
***** Task2 *********************************************************
You should write a function that will receive a positive integer and return: "Fizz" if the number is divisible
by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").
*********************************************************************
"""


def checkio(num: int) -> str:
    return 'Fizz' if num % 3 == 0 else str(num)


# These "asserts" are used for self-checking
assert checkio(3) == "Fizz"
assert checkio(7) == "7"
assert checkio(27) == "Fizz"
assert checkio(0) == "Fizz"
