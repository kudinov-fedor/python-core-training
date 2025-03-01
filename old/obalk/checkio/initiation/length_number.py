"""
You have a non-negative integer. Try to find out how many digits it has.

Input: A non-negative integer.

Output: An integer.

Examples:

assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2
"""

import math


def number_length(value: int) -> int:
    return len(str(value))


def number_length_math(value: int) -> int:
    return int(math.log10(max(1, value))) + 1
