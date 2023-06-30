"""
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

- If one of the symbols is not in the given word - your function should return False.
- If two seeking symbols are the same - your function should return False.

Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first,
 and the third is a symbol (str) that should go after the first one.
Output: A logic value (bool).
"""


def goes_after(word: str, first: str, second: str) -> bool:
    for i in range(len(word)-1):
        if word[i] == first and word[i+1] == second:
            return True
    return False


def goes_after_2_0(word: str, first: str, second: str) -> bool:
    splitted = word.split(first)
    if any(item.startswith(second) for item in splitted[1:]):
        return True
    else:
        return False


def goes_after_3_0(word: str, first: str, second: str) -> bool:
    substr_to_find = first + second
    res = substr_to_find in word
    return res


if __name__ == '__main__':
    print("Example:")
    print(goes_after("world", "w", "o"))
    print(goes_after("", "w", "o"))
    print(goes_after_2_0("world", "w", "o"))
    print(goes_after_2_0("", "w", "o"))
    print(goes_after_3_0("world", "w", "o"))
    print(goes_after_3_0("", "w", "o"))
    print(goes_after_2_0("partial", "a", "r"))
    print(goes_after_2_0("partial", "a", "l"))
    print(goes_after_2_0("world", "d", "w"))
