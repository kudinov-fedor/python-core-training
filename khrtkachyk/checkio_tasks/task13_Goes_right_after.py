"""
In a given string you need to check if one symbol goes right after another. If so - return True, otherwise - False.

- If one of the symbols is not in the given word - your function should return False.
- If two seeking symbols are the same - your function should return False.

Input: Three arguments. The first one is a given string (str), second is a symbol (str) that should go first,
 and the third is a symbol (str) that should go after the first one.
Output: A logic value (bool).
"""


def goes_after(word: str, first: str, second: str) -> bool:
    for i, ch in enumerate(word[:-1]):
        if word[i] == first and word[i+1] == second:
            return True
    return False


def goes_after_2_0(word2: str, first2: str, second2: str) -> bool:
    splitted = word2.split(first2, 1)
    if splitted[-1].startswith(second2):
        return True
    else:
        return False


def goes_after_3_0(word3: str, first3: str, second3: str) -> bool:
    substr_to_find = first3 + second3
    res = substr_to_find in word3
    return res


if __name__ == '__main__':
    print("Example:")
    print(goes_after("world", "w", "o"))
    print(goes_after("", "w", "o"))
    print(goes_after_2_0("world", "w", "o"))
    print(goes_after_2_0("", "w", "o"))
    print(goes_after_3_0("world", "w", "o"))
    print(goes_after_3_0("", "w", "o"))
