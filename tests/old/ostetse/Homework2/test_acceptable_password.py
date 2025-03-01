import pytest


def is_acceptable_password(password: str) -> bool:
    """
    The verification condition is:
    - the length should be bigger than 6.
    Input: A string (str).
    Output: A logic value (bool).
    """
    return len(password) > 6


def test_is_acceptable_password():
    assert is_acceptable_password("short") is False
    assert is_acceptable_password("muchlonger") is True
    assert is_acceptable_password("ashort") is False
