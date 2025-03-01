"""
Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.

Input: An integer.

Output: Bool.

Example:

assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True
"""


def is_even(number: int) -> bool:
    return number % 2 != 1
