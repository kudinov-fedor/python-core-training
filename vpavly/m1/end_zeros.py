"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.
"""


# def end_zeros(num: int) -> int:
#     return beginning_zeros(str(num)[::-1])


def end_zeros(num: int) -> int:
    string_num = str(num)[::-1]
    for zeros, i in enumerate(string_num):
        if i != '0':
            return zeros
        if zeros == len(string_num) - 1:
            return zeros + 1
