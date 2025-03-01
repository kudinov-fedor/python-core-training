import pytest
from checkio_tasks.task_15_Sum_Numbers import sum_numbers
"""
In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.

Input: A string (str).
Output: An integer (int).
"""


@pytest.mark.parametrize(["text", "res"], [
    ("hi", 0),
    ("who is 1st here", 0),
    ("my numbers is 2", 2),
    ("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year", 3755),
    ("5 plus 6 is", 11),
    ("", 0)
])
def test_sum_numbers(text, res):
    assert sum_numbers(text) == res
