"""
***** Task1 **********************************************************
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same
- your function should return False.
**********************************************************************
"""


def goes_after(word: str, first: str, second: str) -> bool:
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
    return result


assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
