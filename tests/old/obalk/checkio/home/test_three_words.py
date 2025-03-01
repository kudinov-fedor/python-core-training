import pytest

from obalk.checkio.home.three_words import is_three_words, is_three_words_bool


@pytest.mark.parametrize("function", [
    is_three_words,
    is_three_words_bool
])
@pytest.mark.parametrize("words, result", [
    ("", False),
    ("some words", False),
    ("1 2 3", False),
    ("0 qwerty a asdfg 2", True),
    ("one two 3 four 5 six 7 eight 9 ten eleven 12", False),
])
def test_duplicate_zeros(function, words, result):
    assert function(words) == result
