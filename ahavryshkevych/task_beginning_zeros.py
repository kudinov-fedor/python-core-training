"""
You have a string that consist only of digits.
You need to find how many zero digits ("0") are at the beginning of the given string.
"""


def beginning_zeros(a: str) -> int:
    count = 0
    for i in a:
        if i == "0":
            count += 1
        else:
            break
    return count
