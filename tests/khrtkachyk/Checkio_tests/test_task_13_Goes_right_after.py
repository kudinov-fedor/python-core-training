import pytest
from checkio_tasks.task13_Goes_right_after import goes_after

"""
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

- If one of the symbols is not in the given word - your function should return False.
- If two seeking symbols are the same - your function should return False.

Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first,
 and the third is a symbol (str) that should go after the first one.
Output: A logic value (bool).
"""


@pytest.mark.parametrize(["word", "first", "second", "res"], [
    ("world", "w", "o", True),
    ("world", "w", "r", False),
    ("world", "l", "o", False),
    ("list", "l", "o", False),
    ("", "l", "o", False),
    ("list", "l", "l", False),
    ("world", "d", "w", False)
])
def test_goes_after(word, first, second, res):
    assert goes_after(word, first, second) is res
