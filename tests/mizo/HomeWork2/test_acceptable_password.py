import pytest
from mizo.task_acceptable_password import is_acceptable_password


@pytest.mark.parametrize("password, expected", [
    ("Maria", False),
    ("Marichka", True),
    ("Mary123", True)
])
def test_acceptable_password(password, expected):
    assert is_acceptable_password(password) is expected
