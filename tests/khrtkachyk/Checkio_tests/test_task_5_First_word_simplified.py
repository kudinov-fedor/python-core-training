"""
You are given a string, and you have to find its first word.
The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.

Input: A string (str).
Output: A string (str).
"""
import pytest
from checkio_tasks.task_5_First_word_simplified import first_word


@pytest.mark.parametrize("text, res", [
    ("Hello world", "Hello"),
    ("a word", "a"),
    ("greeting from CheckiO Planet", "greeting"),
    ("hi", "hi")
])
def test_backward_string(text, res):
    assert first_word(text) == res
