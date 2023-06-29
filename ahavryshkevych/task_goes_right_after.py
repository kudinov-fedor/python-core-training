"""In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
If one of the symbols is not in the given word - your function should return False.
If two seeking symbols are the same - your function should return False.
Input: Three arguments. The first one is a given string (str),
second is a symbol (str) that should go first, and the third is a symbol (str) that should go after the first one.
"""


def goes_after(word: str, first: str, second: str) -> bool:
    both_present = first in word and second in word
    non_equality_check = first != second
    i, j = word.find(first), word.find(second)

    if non_equality_check and both_present:
        for i, j in zip(word, word[1:]):
            # I Wanted to return this expression, as you have taught, buy for some reason it returns False
            # I have to figure out why this happens
            if i == first and j == second:
                return True
    return False
