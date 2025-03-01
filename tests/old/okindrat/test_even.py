# Your function should return True if the number is even, and False if the number is odd.

def is_even(num: int) -> bool:
    return num % 2 == 0


def test_even():
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
