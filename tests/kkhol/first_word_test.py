from kkhol.first_word import first_word

import pytest

@pytest.mark.parametrize("text, word", [
    ('Hello world', 'Hello'),
    ('Nice to meet you', 'Nice'),
    ('My name is nice', 'My'),
    ('I love candy', 'I')
])
def test_first_word(text, word):
    assert first_word(text) == word


@pytest.mark.parametrize("text, word", [
    ('Nice to meet you', 'to'),
    ('Nice to meet you', ''),
    ('Nice to meet you', 'Nice to'),
    ('Nice to meet you', 'N'),
    ('Nice to meet you', 'N ice'),
])
def test_not_first_word(text, word):
    assert first_word(text) != word
