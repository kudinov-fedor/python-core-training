import pytest

from tlazu.First_word import first_word

@pytest.mark.parametrize("sentence, result", [
    ("Hello world", "Hello"),
    ("a word", "a"),
    ("greeting from CheckiO Planet", "greeting"),
    ("hi", "hi"),
])

def first_word(text, result):
    assert first_word(text) == result