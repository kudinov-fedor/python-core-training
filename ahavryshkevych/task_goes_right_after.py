"""In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
If one of the symbols is not in the given word - your function should return False.
If two seeking symbols are the same - your function should return False.
Input: Three arguments. The first one is a given string (str),
second is a symbol (str) that should go first, and the third is a symbol (str) that should go after the first one.
"""


def goes_after(word: str, first: str, second: str) -> bool:
    both_present = first in word and second in word
    non_equality_check = first != second

    if not (non_equality_check and both_present):
        return False
    for i, j in zip(word, word[1:]):
        if i == first and j == second:
            return True
    return False


def goes_after2(word: str, first: str, second: str):
    return str(first + second) in word


def goes_after3(word: str, first: str, second: str):
    return any(el == (first, second) for el in zip(word, word[1:]))
