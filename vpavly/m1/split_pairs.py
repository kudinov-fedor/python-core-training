"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.
"""


def split_pairs(a: str) -> list:
    b = a + '_' if len(a) % 2 else a
    return list(item[0] + item[1] for item in zip(b[::2], b[1::2]))
