"""
Find the nearest value to the given one.

You are given a set of integers and a value for which you need to find the nearest one.

For example, we have the following sequence of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. If we sort this sequence in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.

A few clarifications:

If 2 numbers are at the same distance, you need to choose the smallest one;
The sequence of numbers is always non-empty;
The given value can be in this sequence, which means that it’s the answer;
The sequence may contain both positive and negative numbers, but they are always integers;
The sequence isn’t sorted and consists only unique numbers.
Input: Two arguments. A set of integers. The sought value as an integer.

Output: An integer.
"""

from typing import Set


def nearest_value(values: Set[int], one: int) -> int:
    result = max(values)
    for value in values:
        diff = abs(result - one)
        temp_diff = abs(value - one)
        if temp_diff < diff:
            result = value
        elif temp_diff == diff:
            result = min(value, result)
    return result


def nearest_value_lambda(values: Set[int], one: int) -> int:
    return min(values, key=lambda n: (abs(one - n), n))


def nearest_value_with_nested_func(values: Set[int], one: int) -> int:
    """
    I found this solution and don't understand the part `value > one` at first
    Then I realized so it kinda creates (abd(), bool) items for each value in values
    and then start to apply this results in `min` function
    since we use min `value > one` is useless here, but I learned that is possible to
    filter, sort, min, max whenever we have `key` parameter to use such chain.
    """

    def distance(value):
        return abs(value - one), value > one

    return min(values, key=distance)
