"""
***** Task3 *********************************************************
You are given a string and you have to find its first word.

The input string consists of only English letters and spaces.
There aren’t any spaces at the beginning and the end of the string.
*********************************************************************
"""
import re

import pytest


def first_word(text: str) -> str:
    return text.split(' ')[0]


@pytest.mark.parametrize(['text', 'expected'], [
    ("Hello world", "Hello"),
    ("a word ", "a"),
    ("greeting from CheckiO Planet", "greeting"),
    ("hi", "hi")
])
def test_first_word(text, expected):
    assert first_word(text) == expected


"""
*********************************************************************
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:
    There can be dots and commas in a string.
    A string can start with a letter or, for example, one/multiple dot(s) or space(s).
    A word can contain an apostrophe and it's a part of a word.
    The whole text can be represented with one word and that's it.
*********************************************************************
"""


def first_word_2nd_version(text: str) -> str:
    word = text.replace('.', " ").split()[0]
    is_coma_in_the_end = any(i for i in [',', '.'] if word.endswith(i))
    return word.removesuffix(word[-1]) if is_coma_in_the_end else word


@pytest.mark.parametrize(['text', 'expected'], [
    ("Hello world", "Hello"),
    (" a word ", "a"),
    ("don't touch it", "don't"),
    ("greetings, friends", "greetings"),
    ("... and so on ...", "and"),
    ("hi", "hi")
])
def test_first_word_2d_version(text, expected):
    assert first_word_2nd_version(text) == expected
