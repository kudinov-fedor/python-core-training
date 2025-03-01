"""
You should write a function that will receive a positive integer and return: "Fizz"
if the number is divisible by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2").

Input: An integer (int).
Output: A string (str).
"""
import pytest
from checkio_tasks.task_4_Fizz import just_fizz


@pytest.mark.parametrize("integer, res", [
    (15, "Fizz"),
    (6, "Fizz"),
    (10, "10"),
    (7, "7"),
])
def test_backward_string(integer, res):
    assert just_fizz(integer) == res
