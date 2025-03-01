"""
You have a string that consist only of digits.
You need to find how many zero digits ("0") are at the beginning of the given string.
"""


def beginning_zeros(text_number: str) -> int:
    # saved to remember lstrip method
    # return len(text_number) - len(text_number.lstrip('0'))  # lstrip delete all the leading characters mentioned in its argument.

    # Solution with for
    count_zero = 0
    for char in text_number:
        if char != "0":
            break
        count_zero += 1
    return count_zero


if __name__ == '__main__':
    beginning_zeros("00")
