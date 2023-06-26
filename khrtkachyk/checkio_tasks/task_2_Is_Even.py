"""
Check if the given number is even or not. Your function should return True if the number is even,
and False if the number is odd.

Input: An integer (int).
Output: Logic value (bool).
"""


def is_even(num: int) -> bool:
    return num % 2 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))
    print(is_even(5))
    print(is_even(0))
