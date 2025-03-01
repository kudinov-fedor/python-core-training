import pytest

from olpopova.homework.homework02.first_word import *


@pytest.mark.parametrize(['text', 'expected'], [
    ("Hello world", "Hello"),
    ("a word ", "a"),
    ("greeting from CheckiO Planet", "greeting"),
    ("hi", "hi")
])
def test_first_word(text, expected):
    assert first_word(text) == expected


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
