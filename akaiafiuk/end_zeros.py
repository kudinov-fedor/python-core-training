"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int
Output: An Int.

Example:
end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
123543000 - 3
"""


def end_zeros(num: int) -> int:
    num_reversed = str(num)[::-1]
    for i, v in enumerate(num_reversed):
        if v != '0':
            return i
        else:
            continue
    return len(num_reversed)


def end_zeros_using_split(num: int) -> int:
    number_list = num.split('1')
    return len(number_list[-1])


if __name__ == '__main__':
    print(end_zeros(100100))
    print(end_zeros(1001000))
    print(end_zeros(0))
    print(end_zeros(1))

