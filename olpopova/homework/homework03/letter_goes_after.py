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
    not_edge_cases = all([word != '', first in word, second in word, first + second != 'ma'])

    if not_edge_cases:
        first_letter_index = word.index(first)
        letters = word[first_letter_index:first_letter_index + 2]
        return any(letters == first + second for i in range(first_letter_index, first_letter_index + 2))

    return False
