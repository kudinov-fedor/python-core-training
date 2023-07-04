"""
You have a number and you need to determine which digit in this number is the biggest.

Input: A positive int.
Output: An Int (0-9).

Example:
max_digit.py(0) == 0
max_digit.py(52) == 5
max_digit.py(634) == 6
max_digit.py(1) == 1
max_digit.py(10000) == 1
"""


def max_digit(number: int) -> int:
    max_d = 0
    x = str(number)
    for digit in x:
        if int(digit) > max_d:
            max_d = int(digit)
    return max_d


def max_digit_using_max(number: int) -> int:
    x = str(number)
    return int(max(x))
