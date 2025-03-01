"""
Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: A list or another Iterable of strings.

Example:

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
"""

from typing import Iterable
import itertools
import operator


def split_pairs(text: str) -> Iterable[str]:
    start = 0
    step = 2
    result = []
    while start < len(text):
        pair = text[start: start + step]
        if len(pair) == step:
            result.append(pair)
        else:
            result.append(f"{pair}_")
        start += step
    return result


def split_pairs_zip(text: str) -> Iterable[str]:
    return [ch1 + ch2 for ch1, ch2 in zip(text[::2], f'{text[1::2]}_')]


def split_pairs_iter_tools(text) -> Iterable[str]:
    """
     map(f, a, b) is

    a, b = iter(a), iter(b)
    while ...: yield f(next(a), next(b))
    """
    it = itertools.chain(text, '_')
    return list(map(operator.add, it, it))
