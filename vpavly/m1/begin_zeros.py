"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits.

Output: An Int.
"""


def beginning_zeros_w_lstrip(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


def beginning_zeros_w_int(number: str) -> int:
    result = 0
    if number:
        int_num = str(int(number))
        result = len(number) - len(int_num) or 1
    return result


def beginning_zeros_w_loop(number: str) -> int:
    for i, num in enumerate(number):
        if num != '0':
            result = i
            break
    else:
        result = len(number)
    return result
