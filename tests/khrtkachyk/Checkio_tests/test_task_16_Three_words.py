import pytest
from checkio_tasks.task_16_Three_words import checkio, checkio_2, checkio_3
"""
You are given a string with words and numbers separated by whitespaces (one space).
The words contain only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string (str) with words.
Output: Logic value (bool).
"""


@pytest.mark.parametrize("func", [checkio, checkio_2, checkio_3])
@pytest.mark.parametrize("words, res", [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("Hi", False),
    ("one two 3 four five six 7 eight 9 ten eleven 12", True)
])
def test_acceptable_password(func, words, res):
    assert func(words) is res
