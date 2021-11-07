"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.
"""


# def end_zeros(num: int) -> int:
#     return beginning_zeros(str(num)[::-1])


def end_zeros(num: int) -> int:
    number = str(num)
    return len(number) - len(number.rstrip('0'))
