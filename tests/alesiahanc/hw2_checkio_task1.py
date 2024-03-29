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
    return f"{first}{second}" in word



if __name__ == '__main__':
    goes_after("world", "w", "o")
