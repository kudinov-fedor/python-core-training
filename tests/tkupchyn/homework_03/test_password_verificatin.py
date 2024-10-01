import pytest
from tkupchyn.homework_03.password_verification import is_acceptable_password


@pytest.mark.parametrize('password,expected',
                         (
                                 ("short", False),
                                 ("short54", True),
                                 ("muchlonger", True),
                                 ("ashort", False),
                                 ("12345678", False),
                                 ("1234567890", True),
                                 ("qwertyui", False)
                         ))
def test_is_acceptable_password(password, expected):
    assert is_acceptable_password(password) == expected
