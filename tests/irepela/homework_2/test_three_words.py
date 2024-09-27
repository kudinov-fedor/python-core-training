import pytest
from irepela.homework_2.three_words import has_three_words_in_sequence


@pytest.mark.parametrize("arg, expected", [
    ("Hello World hello", True),
    ("He is 123 man", False),
    ("1 2 3 4", False),
    ("bla bla bla bla", True),
    ("Hi", False),
    ("one two 3 four five six 7 eight 9 ten eleven 12", True)
])
def test_three_words(arg, expected):
    assert has_three_words_in_sequence(arg) is expected
