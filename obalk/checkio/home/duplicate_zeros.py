"""
"Sometimes, zeros resemble very tasty donut. And every time we finish a donut, we want another, and then another, and then another..."

You are given a list of integers. Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...) all zeros (think about donuts ;-P) and return the result as any Iterable. Let's look on the example:

[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]

Input: A list of integers.

Output: A list on another Iterable (tuple, generator, iterator) of integers.
"""


from typing import List, Iterable


def duplicate_zeros(donuts: List[int]) -> Iterable[int]:
    # your code here
    result = []
    for donut in donuts:
        if donut == 0:
            result.append(donut)
        result.append(donut)

    return result


print(duplicate_zeros([1, 0, 2, 0]))
