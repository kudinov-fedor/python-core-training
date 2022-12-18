"""
You are given a list of integers. Your task in this mission is to find, how many times the sorting direction was changed in the given list. If the elements are equal - the previous sorting direction remains the same, if the sequence starts from the same elements - look for the next different to determine the sorting direction.

There are three sorting directions:

on the chunk 1, 2, 2 - up (increasing);
on the chunk 2, 1 - down (decreasing);
and on the chunk 1, 2, 2 - up again.
So, you have two points of changing the sorting direction: #1 - from up to down, and #2 - from down to up. That's the result your function should return.
Input: A list of integers.

Output: Integer.
"""
from typing import List


def changing_direction(elements: List[int]) -> int:
    if not elements:
        return 0
    first_number = elements[0]
    sign = 0
    changes = 0
    first_change = True
    for number in elements[1:]:
        if first_number != number and first_change:
            sign = (first_number - number) < 0
            first_change = False
        if first_number < number:
            if not sign:
                changes += 1
            sign = 1
        elif first_number > number:
            if sign:
                changes += 1
            sign = 0
        else:
            continue
        first_number = number

    return changes


def changing_direction_zip(elements: List[int]) -> int:
    initial_direction = count = 0
    for a, b in zip(elements, elements[1:]):
        current_direction = a - b
        if current_direction:
            if current_direction * initial_direction < 0:
                count += 1
            initial_direction = current_direction
    return count
