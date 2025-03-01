"""
In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

Input: List.

Output: Iterable.

Example:

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []
"""

from typing import Any, List, Iterable


def replace_first(items: List[Any]) -> Iterable:
    if items:
        first_value = items.pop(0)
        items.append(first_value)
    return items


def replace_first_slice(items: list) -> list:
    return items[1:] + items[:1]
