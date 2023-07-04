import pytest

from olpopova.homework.homework03.letter_goes_after import goes_after


@pytest.mark.parametrize(['word', 'first','second', 'expected'], [
    ("world", "w", "o", True,),
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
