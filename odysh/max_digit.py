"""
You have a number and you need to determine which digit in this number is the biggest.
"""


def max_digit(number: int) -> int:
    return int(max(list(str(number))))