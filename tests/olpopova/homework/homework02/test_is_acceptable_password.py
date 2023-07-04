import pytest

from olpopova.homework.homework02.is_acceptable_password import *


@pytest.mark.parametrize(['password', 'expected'], [
    ("short", False),
    ("short54", True),
    ("muchlonger", False),
    ("ashort", False),
    ("muchlonger5", True),
    ("sh5", False)
])
def test_function(password, expected):
    assert is_acceptable_password(password) is expected


@pytest.mark.parametrize(['password', 'expected'], [
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
def test_function_4th(password, expected):
    assert is_acceptable_password_4th_edition(password) is expected


@pytest.mark.parametrize(['password', 'expected'], [
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
def test_function_5th(password, expected):
    assert is_acceptable_password_5th_edition(password) is expected
