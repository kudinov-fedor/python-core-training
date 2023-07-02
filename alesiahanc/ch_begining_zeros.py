"""
You have a string that consist only of digits.
You need to find how many zero digits ("0") are at the beginning of the given string.
"""


def beginning_zeros(text_number: str) -> int:
    # your code here
    return len(text_number) - len(text_number.lstrip('0'))  # lstrip delete all the leading characters mentioned in its argument.
