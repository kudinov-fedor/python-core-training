"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: An iterable of strings.
"""
from typing import Iterable


def split_pairs(a: str) -> Iterable:
    a = a + '_' if len(a) % 2 != 0 else a
    b = []
    for i in range(0, len(a) - 1, 2):
        b.append(a[i] + a[i + 1])
    return b


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))
