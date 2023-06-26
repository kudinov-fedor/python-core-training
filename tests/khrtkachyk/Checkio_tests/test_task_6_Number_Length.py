"""
You have a non-negative integer. Try to find out how many digits it has.

Input: A non-negative integer (int).
Output: An integer (int)
"""
import pytest
from checkio_tasks.task_6_Number_Length import number_length


@pytest.mark.parametrize("number, res", [
    (10, 2),
    (0, 1),
    (4444, 4),
    (123, 3)
])
def test_number_length(number, res):
    assert number_length(number) == res
