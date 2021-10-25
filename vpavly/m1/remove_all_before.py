"""
Not all of the elements are important. What you need to do here is to remove from the list all of the elements before the given one.

example

For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove all elements that go before 3 - which is 1 and 2.

We have two edge cases here: (1) if a cutting element cannot be found, then the list shoudn't be changed. (2) if the list is empty, then it should remain empty.

Input: List and the border element.

Output: Iterable (tuple, list, iterator ...).

"""
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        items = items[items.index(border):] if len(items) > 1 else items
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
