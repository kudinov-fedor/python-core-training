"""
You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list.
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

Input: A list of integers.

Output: An iterable of integers.
"""
from typing import List


def non_unique_elements(numbers: List[int]) -> List[int]:
    return [number for number in numbers if numbers.count(number) > 1]
