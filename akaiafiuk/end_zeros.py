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
    to_be_replaced = ['2', '3', '4', '5', '6', '7', '8', '9']
    for item in to_be_replaced:
        num_str = num_str.replace(item, '1')
    number_list = num_str.split('1')
    return len(number_list[-1])


def end_zeros_using_zip(num: int) -> int:
    num_str = str(num)
    for left, right in zip('23456789', '11111111'):
        num_str = num_str.replace(left, right)
    number_list = num_str.split('1')
    return len(number_list[-1])


def end_zeros_using_generator(num: int) -> int:
    num_str = str(num)
    num_str_replaced = ''.join(i if i == '0' else '1' for i in num_str)
    number_list = num_str_replaced.split('1')
    return len(number_list[-1])


def end_zeros_using_translate(num: int) -> int:
    num_str = str(num)
    my_table = num_str.maketrans('23456789', '11111111')
    num_str = num_str.translate(my_table)
    number_list = num_str.split('1')
    return len(number_list[-1])
