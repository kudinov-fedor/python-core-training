"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit, but cannot consist of just digits.

Input: A string (str).
Output: A logic value (bool).
"""
import pytest
from checkio_tasks.task_9_Acceptable_Pass_v_III import is_acceptable_password


@pytest.mark.parametrize("passw, res", [
    ("short", False),
    ("muchlongerwithnodigit", False),
    ("short1", False),
    ("muchlonger5", True),
    ("acceptable6_", True),
    ("1234567!", False)
])
def test_acceptable_pass(passw, res):
    assert is_acceptable_password(passw) == res
