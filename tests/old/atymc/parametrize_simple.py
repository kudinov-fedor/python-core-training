import pytest


@pytest.mark.parametrize('text, expected', [
    ('Hello world', 'Hello'),
    ('a word', 'a'),
    ('greetings from new planet', 'greetings'),
])
def test_first_word(text, expected):
    assert text.split(" ")[0] == expected
