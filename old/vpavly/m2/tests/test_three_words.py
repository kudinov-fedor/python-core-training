import pytest

from vpavly.m2.three_words import three_words_in_succession


@pytest.mark.parametrize('a, expected', [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("Hi", False)
])
def test_three_words_in_succession(a, expected):
    assert three_words_in_succession(a) == expected
