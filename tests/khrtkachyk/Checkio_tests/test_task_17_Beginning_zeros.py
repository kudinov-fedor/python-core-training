import pytest
from checkio_tasks.task_17_Beginning_zeros import beginning_zeros, beginning_zeros2, beginning_zeros3
"""
You have a string that consist only of digits. You need to find how many zero
digits ("0") are at the beginning of the given string.

Input: A string (str), that consists of digits.
Output: An integer (int).
"""


@pytest.mark.parametrize("func", [beginning_zeros, beginning_zeros2, beginning_zeros3])
@pytest.mark.parametrize("string, res", [
    ("10", 0),
    ("100", 0),
    ("001", 2),
    ("100100", 0),
    ("001001", 2),
    ("", 0)
])
def test_beginning_zeros(func, string, res):
    assert func(string) == res
