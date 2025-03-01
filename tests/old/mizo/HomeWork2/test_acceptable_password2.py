import pytest
from mizo.task_acceptable_password2 import is_acceptable_password


@pytest.mark.parametrize("password, expected", [
    ("short", False),
    ("123456789", False),
    ("abcdefg", False),
    ("Password123", True)
])
def test_is_acceptable_password(password, expected):
    assert is_acceptable_password(password) is expected
