"""
****** Task2 ********************************************************
Max Digit

You have a number and you need to determine which digit in this number is the biggest.
*********************************************************************
"""
import pytest


def max_digit(value: int) -> int:
    return int(max(str(value)))


@pytest.mark.parametrize(['value', 'expected'], [
    (0, 0),
    (52, 5),
    (634, 6),
    (1, 1),
    (10000, 1),
    (3579, 9)
])
def test_max_digit(value, expected):
    assert max_digit(value) == expected
