import pytest
from checkio_tasks.task_19_First_word_2_0 import first_word

"""
I might see a simplified version of this mission already First Word (simplified).
This mission is a little more complex as not only English letters can be in the given string.

You are given a string where you have to find its first word.
When solving a task pay attention to the following points:

- There can be dots and commas in a string.
- A string can start with a letter or, for example, one/multiple dot(s) or space(s).
- A word can contain an apostrophe, and it's a part of a word.
- The whole text can be represented with one word and that's it.

Input: A string (str).
Output: A string (str).
"""


@pytest.mark.parametrize("string, res", [
    ("Hello world", "Hello"),
    (" a word ", "a"),
    ("don't touch it", "don't"),
    ("greetings, friends", "greetings"),
    ("... and so on ...", "and"),
    ("hi", "hi"),
    ("Hello.World", "Hello")
])
def test_first_word(string, res):
    assert first_word(string) == res
