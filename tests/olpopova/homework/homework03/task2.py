"""
****** Task2 ********************************************************
Max Digit

You have a number and you need to determine which digit in this number is the biggest.
*********************************************************************
"""


def max_digit(value: int) -> int:
    return int(max(str(value)))


assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(1000) == 1
assert max_digit(3579) == 9
