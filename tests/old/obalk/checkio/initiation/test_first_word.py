import pytest

from obalk.checkio.initiation.find_first_word import first_word


@pytest.mark.parametrize("sentence, result", [
    ("Hello world", "Hello"),
    ("a word", "a"),
    ("greeting from CheckiO Planet", "greeting"),
    ("hi", "hi"),
])
def test_first_word(sentence, result):
    assert first_word(sentence) == result
