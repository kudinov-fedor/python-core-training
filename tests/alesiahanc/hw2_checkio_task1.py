"""
Task "Goes Right After (simplified)".
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

If one of the symbols is not in the given word - your function should return False. If two seeking symbols are the same
- your function should return False.

Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first,
and the third is a symbol (str) that should go after the first one.

Output: A logic value (bool).
"""


def goes_after(word: str, first: str, second: str) -> bool:
    index_first_item = word.find(first)
    index_second_item = word.find(second)
    if index_first_item == -1 and index_second_item == -1:
        return False
    elif first == second:
        return False
    elif index_second_item != index_first_item + 1:
        return False
    else:
        return True
