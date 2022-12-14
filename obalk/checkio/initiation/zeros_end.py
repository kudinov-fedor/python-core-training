"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:

assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
"""


def end_zeros(number: int) -> int:
    count = 0
    for number in str(number)[-1::-1]:
        if number == "0":
            count += 1
        else:
            break
    return count


def end_zeros_strip_len(number: int) -> int:
    value = str(number)
    return len(value) - len(value.rstrip('0'))
