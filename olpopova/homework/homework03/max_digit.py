"""
*********************************************************************
Max Digit

You have a number and you need to determine which digit in this number is the biggest.
*********************************************************************
"""


def max_digit(value: int) -> int:
    return int(max(str(value)))
