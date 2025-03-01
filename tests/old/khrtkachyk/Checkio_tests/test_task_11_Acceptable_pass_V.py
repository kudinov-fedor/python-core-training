"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit, but it cannot consist of just digits;
- having numbers or containing just numbers does not apply to the password longer than 9;
- a string should not contain the word "password" in any case.
Input: A string (str).
Output: A logic value (bool).
"""
import pytest
from checkio_tasks.task_11_Acceptable_pass_V import is_acceptable_password


@pytest.mark.parametrize("passwd, res", [
    ("short", False),
    ("short54", True),
    ("muchlonger", True),
    ("ashort", False),
    ("muchlonger5", True),
    ("sh5", False),
    ("1234567", False),
    ("12345678910", True),
    ("password12345", False),
    ("PASSWORD12345", False),
    ("pass1234word", True)
])
def test_acceptable_password(passwd, res):
    assert is_acceptable_password(passwd) == res
