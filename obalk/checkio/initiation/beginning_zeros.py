"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.

Example:

assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
"""


def beginning_zeros(line: str) -> int:
    return len(line) - len(line.lstrip('0'))
