"""
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

Example:

assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([2, 1, 1, 1]) == False
"""

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) < 2:
        return True
    first_element = elements[0]
    return all(element == first_element for element in elements)


def all_the_same_set(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


print(all_the_same_set([1, 2, 1]))
