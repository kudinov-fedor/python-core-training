import pytest

from tlazu.Acceptable_Password import is_acceptable_password

@pytest.mark.parametrize("number, result", [
    ("Pass", False),
    ("", False),
    ("RightPassword", True)
])
def test_and_zeros(number, result):
    assert is_acceptable_password(number)==result