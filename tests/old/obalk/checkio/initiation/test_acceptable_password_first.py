import pytest

from obalk.checkio.initiation.acceptable_password_first import is_acceptable_password


@pytest.mark.parametrize("number, result", [
    ("MyPass", False),
    ("", False),
    ("Macbook", True)
])
def test_end_zeros(number, result):
    assert is_acceptable_password(number) == result
