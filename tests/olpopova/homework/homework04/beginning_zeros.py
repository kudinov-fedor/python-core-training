"""
**********************************************************************
Beginning Zeros

You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the
given string.
**********************************************************************
"""


def beginning_zeros(a: str) -> int:
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


# These "asserts" are used for self-checking
def test_function():
    assert beginning_zeros("100") == 0
    assert beginning_zeros("001") == 2
    assert beginning_zeros("100100") == 0
    assert beginning_zeros("001001") == 2
    assert beginning_zeros("012345679") == 1
    assert beginning_zeros("0000") == 4
