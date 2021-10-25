"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.
"""


def end_zeros(num: int) -> int:
    res = 0
    for i in str(num)[::-1]:
        if i != '0': break
        res += 1
    return res


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))
