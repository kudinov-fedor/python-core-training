import pytest

from keyword import iskeyword, kwlist


@pytest.mark.parametrize('word', kwlist)
def test_keywords(word):
    assert iskeyword(word)


@pytest.mark.parametrize('word', [
    'here',
    'not a',
    'keyword',
    1,
])
def test_negative_keywords(word):
    assert not iskeyword(word)
