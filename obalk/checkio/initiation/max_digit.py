"""
You have a number and you need to determine which digit in this number is the biggest.

Input: A positive integer.

Output: An integer (0-9).

Examples:

assert max_digit.py(0) == 0
assert max_digit.py(52) == 5
assert max_digit.py(634) == 6
assert max_digit.py(1) == 1
"""


def max_digit(number: int) -> int:
    return int(max(str(number)))


def max_digit_div(number: int) -> int:
    biggest_digit = 0
    while number:
        number, digit = divmod(number, 10)
        biggest_digit = max(biggest_digit, digit)
    return biggest_digit
