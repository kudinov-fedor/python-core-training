"""
You should return a given string in reverse order.

Input: A string.

Output: A string.
"""


def backward_string_w_reversed(val: str) -> str:
    return "".join(list(reversed(val)))


def backward_string_w_slice(val: str) -> str:
    return val[::-1]
