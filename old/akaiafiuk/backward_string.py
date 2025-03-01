"""
You should return a given string in reverse order.
Input: A string.
Output: A string.
"""


def backward_string(val: str) -> str:
    return val[::-1]


def backward_string_using_reversed(val: str) -> str:
    return ''.join(reversed(val))
