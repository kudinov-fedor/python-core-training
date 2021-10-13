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
            number_of_zeroes +=1
    return number_of_zeroes


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
