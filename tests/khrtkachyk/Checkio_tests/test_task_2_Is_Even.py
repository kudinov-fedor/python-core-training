"""
Check if the given number is even or not. Your function should return True if the number is even,
and False if the number is odd.

Input: An integer (int).
Output: Logic value (bool).
"""
import pytest
from checkio_tasks.task_2_Is_Even import is_even


@pytest.mark.parametrize("num, res", [
    (2, True),
    (5, False),
    (0, True),
])
def test_is_even(num, res):
    assert is_even(num) == res
