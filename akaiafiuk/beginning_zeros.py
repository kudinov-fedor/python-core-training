"""
You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of
the given string.

Input: A string, that consist of digits.
Output: An Int.

Example:
beginning_zeros('100') == 0
beginning_zeros('001') == 2
beginning_zeros('100100') == 0
beginning_zeros('001001') == 2
beginning_zeros('012345679') == 1
beginning_zeros('0000') == 4
"""


def beginning_zeros(number: str) -> int:
    number_of_zeros = 0
    for x in number:
        if x == '0':
            number_of_zeros += 1
        else:
            break
    return number_of_zeros


def beginning_zeros_using_split(number: str) -> int:
    number_list = number.split('1')
    return len(number_list[0])
