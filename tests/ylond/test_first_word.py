import pytest

from ylond.find_first_word import first_word


@pytest.mark.parametrize("text, expected", [
    ("", ""),
    ("1 2 5", "1"),
    ("-5e, exponent", "-5e,"),
    ("Hi Harry", "Hi"),
    ("NONE exception", "NONE"),
    ("First_word", "First_word")
])
def test_first_word(text, expected):
    assert first_word(text) == expected
