import pytest

from khrynchuk.task_get_first_word import first_word


@pytest.mark.parametrize("text, word", [
    ("Hello world", "Hello"),
    ("a word", "a"),
    ("hi", "hi"),
])
def test_first_word(text, word):
    assert first_word(text) == word
