import pytest
from irepela.homework_3.acceptable_password import check_password


@pytest.mark.parametrize("a, expected", [
    ("short", False),
    ("short54", True),
    ("muchlonger", True),
    ("ashort", False),
    ("password", False),
    ("12345678", False),
])
def test_common_words(a, expected):
    assert check_password(a) == expected
