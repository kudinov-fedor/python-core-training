"""
You are given a string and you have to find its first word.

Input: A string.

Output: A string.
"""


def first_word(text: str) -> str:
    return str(text.split()[0]) if text else ''
