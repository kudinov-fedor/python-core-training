import pytest

from olpopova.homework.homework03.three_words import *


@pytest.mark.parametrize(['words', 'expected'], [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 bla 3 4", False),
    ("bla 1 bla bla bla", True),
    ("Hi", False),
    ('one two 3 four five 6 seven eight 9 ten eleven 12', False)
])
def test_checkio(words, expected):
    assert checkio(words) is expected
