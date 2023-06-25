"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit, but it cannot consist of just digits;
- if the password is longer than 9 - previous rule (about one digit), is not required.
Input: A string (str).
Output: A logic value (bool).
"""
import pytest
from checkio_tasks.task_10_Acceptable_Pass_v_IV import is_acceptable_password


@pytest.mark.parametrize("passwd, res", [
    ("short", False),
    ("short54", True),
    ("muchlonger", True),
    ("ashort", False),
    ("notshort", False),
    ("muchlonger5", True),
    ("sh5", False),
    ("1234567", False),
    ("12345678910", True)
])
def test_acceptable_pass(passwd, res):
    assert is_acceptable_password(passwd) == res
