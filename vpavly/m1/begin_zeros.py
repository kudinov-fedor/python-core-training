"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.
"""


def beginning_zeros(number: str) -> int:
    for zeros, i in enumerate(number):
        if i != '0':
            return zeros
        if zeros == len(number) - 1:
            return zeros + 1
    return 0
