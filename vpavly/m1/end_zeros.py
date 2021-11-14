"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.
"""


def end_zeros_w_rstrip(num: int) -> int:
    number = str(num)
    return len(number) - len(number.rstrip('0'))


def end_zeros_w_loop(number: int) -> int:
    reversed_num = str(number)[::-1]
    for index, number in enumerate(reversed_num):
        if number != '0':
            result = index
            break
    else:
        result = len(number)
    return result
