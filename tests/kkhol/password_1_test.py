from kkhol.password_1 import is_acceptable_password


import pytest


@pytest.mark.parametrize("password, expected", [
    ('3, 2', False),
    ('', False),
    ('1234567', True),
    ('123456', False)
])
def test_is_acceptable_password(password, expected):
    assert is_acceptable_password(password) == expected