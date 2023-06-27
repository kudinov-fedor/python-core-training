"""
***** Task4 *********************************************************
You have a non-negative integer. Try to find out how many digits it has.
*********************************************************************
"""
from math import log10, floor, ceil


def number_length(value: int) -> int:
    return len(str(value))


def number_length_with_log_10(value: int) -> int:
    # edge cases
    if value == 0:
        return 1

    # intermediate values
    log_10 = log10(value)
    value_threshold = log_10 - floor(log_10) < 0.5
    long_float = value > len('a' * 14)

    # final steps
    char_length_gt_15 = ceil(log_10)
    char_length_lt_15 = round(log_10) + 1 if value_threshold else ceil(log_10)

    return char_length_gt_15 if long_float else char_length_lt_15


def number_length_with_div_mod(value: int) -> int:
    qty = 1

    # edge cases
    if value == 0:
        return qty
    elif value > len('9' * 16):
        return number_length(value)

    # final steps
    while divmod(value, 10)[0] != 0:
        value /= 10
        qty += 1

    return qty


# These "asserts" are used for self-checking
for i in range(1, 50):
    val = int("9" * i)
    assert number_length(val) == number_length_with_log_10(val) == number_length_with_div_mod(val)
