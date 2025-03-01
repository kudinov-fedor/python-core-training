"""
**********************************************************************
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same
- your function should return False.
**********************************************************************
"""


def goes_after(word: str, first: str, second: str) -> bool:
    return any(word[i : i + 2] == first + second for i in range(0, len(word)))      # or   first + second in word


def goes_after_2nd(word: str, first: str, second: str) -> bool:
    return first in word and word.find(second) - word.find(first) == 1
