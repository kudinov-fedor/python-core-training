"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.
"""


def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))
