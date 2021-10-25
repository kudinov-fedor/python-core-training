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
    num_str = str(num)
    convert_to_ones = num_str.replace('2', '1').replace('3', '1').replace('4', '1').\
        replace('5', '1').replace('6', '1').replace('7', '1').replace('8', '1').replace('9', '1')
    number_list = convert_to_ones.split('1')
    return len(number_list[-1])
