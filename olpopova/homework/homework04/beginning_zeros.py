"""
**********************************************************************
Beginning Zeros

You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the
given string.
**********************************************************************
"""


def beginning_zeros(a: str) -> int:
    return len(a) - len(a.lstrip('0'))


def beginning_zeros_forloop(a: str) -> int:
    length = 0
    # edge case
    if a[0] != '0':
        return length
    for i in a:
        if i == '0':
            length += 1
        else:
            break
    return length
