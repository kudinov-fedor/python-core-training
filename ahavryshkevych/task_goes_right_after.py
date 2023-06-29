"""In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.
If one of the symbols is not in the given word - your function should return False.
If two seeking symbols are the same - your function should return False.
Input: Three arguments. The first one is a given string (str),
second is a symbol (str) that should go first, and the third is a symbol (str) that should go after the first one.
"""


def goes_after(word: str, first: str, second: str) -> bool:
    i, j = word.find(first), word.find(second)
    if first != second and (first or second in word):
        if i + 1 == j:
            return True
        else:
            return False
    else:
        return False
