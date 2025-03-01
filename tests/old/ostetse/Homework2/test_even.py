import pytest


def is_even(num: int) -> bool:
    """
    Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.
    Input: An integer (int).
    Output: Logic value (bool).
    """
    return num % 2 == 0


def test_is_even():
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True