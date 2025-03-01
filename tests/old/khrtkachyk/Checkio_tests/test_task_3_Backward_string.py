"""
You should return a given string in reverse order.

Input: A string (str).
Output: A string (str).
"""
import pytest
from checkio_tasks.task_3_Backward_string import backward_string


@pytest.mark.parametrize("value, res", [
    ("val", "lav"),
    ("", ""),
    ("ohho", "ohho"),
    ("123456789", "987654321"),
])
def test_backward_string(value, res):
    assert backward_string(value) == res
