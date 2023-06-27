"""
***** Task1 **********************************************************
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same
- your function should return False.
**********************************************************************
"""
import pytest


@pytest.mark.parametrize(['word', 'first', 'second', 'expected'], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False)
])
def test_goes_after(word, first, second, expected):
    result = False

    # edge cases
    if len(word) == 0:
        return result
    first_index = word.index(first)
    if first_index == len(word) - 1:
        return result

    # final steps
    follow_index = first_index + 1
    result = first == word[first_index] and second == word[follow_index]
    assert result is expected
