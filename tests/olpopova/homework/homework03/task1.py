"""
***** Task1 **********************************************************
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same
- your function should return False.
**********************************************************************
"""
import pytest


def goes_after(word: str, first: str, second: str) -> bool:
    # edge cases
    if len(word) == 0 or first not in word:
        return False

    first_index = word.index(first)
    if first_index == len(word) - 1:
        return False

    return any(word[i] == first and word[i + 1] == second for i in range(0, len(word)))


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
