"""
****** Task2 ********************************************************
Max Digit

You have a number and you need to determine which digit in this number is the biggest.
*********************************************************************
"""
import pytest


@pytest.mark.parametrize(['value', 'expected'], [
    (0, 0),
    (52, 5),
    (634, 6),
    (1, 1),
    (10000, 1),
    (3579, 9)
])
def max_digit(value, expected):
    digit = 0

    for i in str(value):
        if digit < int(i):
            digit = int(i)

    assert digit == expected
