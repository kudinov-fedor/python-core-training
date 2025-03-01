"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean.
"""


def is_all_upper(text: str) -> bool:
    return text.upper() == text
