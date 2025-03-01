"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence. It can be only one.

Input: non empty list of strings.

Output: a string.

Example:

assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
"""

from collections import Counter
from typing import List


def most_frequent(letters: List[str]) -> str:
    return Counter(letters).most_common(1)[0][0]


def most_frequent_with_max(data: List[str]):
    return max(set(data), key=data.count)
