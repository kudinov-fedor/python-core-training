"""
So this mission is the easiest one. Write a function that will receive 2 numbers as input and it should return
the multiplication of these 2 numbers.

Input: Two arguments. Both are of type int
Output: Int.

Example:
mult_two(2, 3) == 6
mult_two(1, 0) == 0
"""


def multiply_two(a, b):
    return a * b


if __name__ == '__main__':
    print("Example:")
    print(multiply_two(3, 2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert multiply_two(3, 2) == 6
    assert multiply_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
