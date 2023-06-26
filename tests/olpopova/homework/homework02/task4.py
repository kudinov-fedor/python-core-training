"""
***** Task4 *********************************************************
You have a non-negative integer. Try to find out how many digits it has.
*********************************************************************
"""
from math import log10, floor, ceil


def number_length(value: int) -> int:
    return len(str(value))


# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2


def number_length2(value: int) -> int:
    return 1 if value == 0 else (ceil(log10(value)) if log10(value) > 1.5 else ceil(log10(value)) + 1)


# These "asserts" are used for self-checking
assert number_length2(10) == 2
assert number_length2(0) == 1
assert number_length2(56890) == 5
assert number_length2(44) == 2
assert number_length2(87860404) == 8
assert number_length2(8786040432) == 10
assert number_length2(999999999999999) == 15


def x(value: int) -> int:
    qty = 1
    if value != 0:
        while divmod(value, 10)[0] != 0:
            value /= 10
            qty += 1
    return qty


# These "asserts" are used for self-checking
assert x(10) == 2
assert x(0) == 1
assert x(56890) == 5
assert x(44) == 2
assert x(87860404) == 8
assert x(8786040432) == 10
assert x(999999999999999) == 15
