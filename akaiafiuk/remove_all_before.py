"""
Not all of the elements are important. What you need to do here is to remove from the list all of the elements before
the given one.

We have two edge cases here:
(1) if a cutting element cannot be found, then the list shoudn't be changed.
(2) if the list is empty, then it should remain empty.

Input: List and the border element.
Output: Iterable (tuple, list, iterator ...).

Example:
remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
"""


def remove_all_before(items: list, border: int) -> list:
    start_index = items.index(border) if border in items else 0
    return items[start_index:]
