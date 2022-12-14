"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.

Example:

assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
"""


def all_upper(text: str) -> bool:
    return not any(letter.islower() for letter in text)


def all_upper_upper(text: str) -> bool:
    return text.upper() == text
