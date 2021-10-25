"""
In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

Input: List.

Output: Iterable.
"""
from typing import Iterable


def replace_first(items: list) -> Iterable:
    # items = items[1:].append(items[0])  # Doesn't work at well :(
    items = items[1:] + [items[0]] if len(items) > 1 else items
    return items


if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3])))
