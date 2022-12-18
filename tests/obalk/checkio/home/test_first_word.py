import pytest

from obalk.checkio.home.first_word import first_word


@pytest.mark.parametrize("words, result", [
    ("Hello world", "Hello"),
    (" a word ", "a"),
    ("don't touch it", "don't"),
    ("greetings, friends", "greetings"),
])
def test_duplicate_zeros(words, result):
    assert first_word(words) == result
