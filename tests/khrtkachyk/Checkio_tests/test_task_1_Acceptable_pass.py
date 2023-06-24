"""
In this mission, you need to create a password verification function.
The verification condition is:
- the length should be bigger than 6.
Input: A string (str).
Output: A logic value (bool).
"""
import pytest
from checkio_tasks.task_1_Acceptable_pass import is_acceptable_password


@pytest.mark.parametrize("password, expected", [
    ("short", False),
    ("muchlonger", True),
    ("ashort", False),
])
def test_is_acceptable_password(password, expected):
    assert is_acceptable_password(password) == expected
