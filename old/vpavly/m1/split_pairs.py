"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.
"""


def split_pairs(text: str) -> list:
    text += '_' if len(text) % 2 else ""
    return list(left + right for (left, right) in zip(text[::2], text[1::2]))
