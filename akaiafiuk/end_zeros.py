"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int
Output: An Int.

Example:
end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""


def end_zeros(num: int) -> int:
    num_reversed = str(num)[::-1]
    number_of_zeroes = 0
    for x in num_reversed:
        if x != '0':
            break
        else:
            number_of_zeroes += 1
    return number_of_zeroes


def end_zeros_using_split(num: int) -> int:
    number_list = num.split('1')
    return len(number_list[-1])
