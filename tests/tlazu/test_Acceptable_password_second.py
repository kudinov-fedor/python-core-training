import pytest

from tlazu.Acceptable_password_second import is_acceptable_password

@pytest.mark.parametrize("number, result", [
    ("Pass", False),
    ("", False),
    ("Right123Password", True)
])
def test_and_zeros(number, result):
    assert is_acceptable_password(number)==result