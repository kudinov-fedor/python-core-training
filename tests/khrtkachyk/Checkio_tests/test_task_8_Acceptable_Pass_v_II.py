"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit.
Input: A string (str).
Output: A logic value (bool).
"""
import pytest
from checkio_tasks.task_8_Acceptable_Pass_v_II import is_acceptable_password


@pytest.mark.parametrize("passw, res", [
    ("short", False),
    ("muchlonger", False),
    ("ashort", False),
    ("muchlonger5", True),
    ("shshs5", False)
])
def test_accept_pass(passw, res):
    assert is_acceptable_password(passw) == res
