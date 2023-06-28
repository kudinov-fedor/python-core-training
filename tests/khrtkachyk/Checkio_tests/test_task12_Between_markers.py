import pytest
from checkio_tasks.task_12_Between_markers import between_markers
"""
You are given a string and two markers (the initial one and final). You have to find a substring enclosed
    between these two markers. But there are a few important conditions.
- The initial and final markers are always different.
- The initial and final markers are always 1 char size.
- The initial and final markers always exist in a string and go one after another.

Input: Three arguments. All of them are strings (str).
        The second and third arguments are the initial and final markers.
Output: A string (str).
"""


@pytest.mark.parametrize(["text", "start", "end", "res"], [
    ("What is >apple<", ">", "<", "apple"),
    ("What is [apple]", "[", "]", "apple"),
    ("What is ><", ">", "<", ""),
    ("[an apple]", "[", "]", "an apple")
])
def test_between_markers(text, start, end, res):
    assert between_markers(text, start, end) == res
