"""
**********************************************************************
Beginning Zeros

You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the
given string.
**********************************************************************
"""


def beginning_zeros(a: str) -> int:
    return len(a) - len(a.lstrip('0'))
