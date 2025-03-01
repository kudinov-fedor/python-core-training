import pytest

from olpopova.homework.homework03.letter_goes_after import goes_after, goes_after_2nd


@pytest.mark.parametrize(['word', 'first', 'second', 'expected'], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False),
    ("camel", "b", "f", False),
    ("partial", "a", "l", True)
])
def test_goes_after(word, first, second, expected):
    assert goes_after(word, first, second) is expected


@pytest.mark.parametrize(['word', 'first', 'second', 'expected'], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("panorama", "a", "n", True),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False),
    ("Almaz", "a", "l", False),
    ('transport', 'r', 't', False),
    ('almaz', 'm', 'a', False),     # very weird case (I`m sure it should be True)
    ('almaz', 'r', 'l', False),
    ('almaz', 'p', 'p', False),
    ('almaz', 'r', 'a', False),
    ('world', 'a', 'r', False),
    ('amazed', 'a', 'z', False)
])
def test_goes_after(word, first, second, expected):
    assert goes_after_2nd(word, first, second) is expected
