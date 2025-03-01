"""
You should write a function that will receive a positive integer and return:

- "Fizz Buzz" if the number is divisible by 3 and by 5;
- "Fizz" if the number is divisible by 3;
- "Buzz" if the number is divisible by 5;
- The number as a string for other cases.

Input: An integer (int).
Output: A string (str).
"""
import pytest
from checkio_tasks.task_7_Fizz_Buzz import checkio


@pytest.mark.parametrize("num, res", [
    (30, "Fizz Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (7, "7")
])
def test_backward_string(num, res):
    assert checkio(num) == res
