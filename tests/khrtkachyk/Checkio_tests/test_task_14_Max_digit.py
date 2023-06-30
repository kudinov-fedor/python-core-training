import pytest
from checkio_tasks.task_14_Max_digit import max_digit

"""
You have a number, and you need to determine which digit in this number is the biggest.

Input: A positive integer (int).
Output: An integer 0-9 (int).
"""


@pytest.mark.parametrize(["value", "res"], [
    (0, 0),
    (52, 5),
    (634, 6),
    (1, 1),
    (10000, 1)
])
def test_max_digit(value, res):
    assert max_digit(value) == res
