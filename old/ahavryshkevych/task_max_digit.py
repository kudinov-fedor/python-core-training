"""
You have a number, and you need to determine which digit in this number is the biggest.
"""


def max_digit(value: int) -> int:
    x = [i for i in str(value)]
    return int(max(x))
