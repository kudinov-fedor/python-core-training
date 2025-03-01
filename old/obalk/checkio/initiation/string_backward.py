"""
You should return a given string in reverse order.

Input: A string.

Output: A string.

Example:

assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"
"""


def backward_string(value: str) -> str:
    return value[::-1]
