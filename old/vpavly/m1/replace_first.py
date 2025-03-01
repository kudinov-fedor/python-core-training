"""
In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

Input: List.

Output: Iterable.
"""


def replace_first(items: list) -> list:
    if len(items):
        items.append(items.pop(0))
    return items
