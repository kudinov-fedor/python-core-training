"""
In a given list the first element should become the last one. An empty list or list with only one element should stay
the same.
Input: List.
Output: Iterable.

Example:
replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
"""


def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items


def replace_last(items: list) -> list:
    if items:
        items.insert(0, items.pop(-1))
    return items
