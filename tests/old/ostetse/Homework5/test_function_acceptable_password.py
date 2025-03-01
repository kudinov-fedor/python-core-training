from tests.old.ostetse.Homework5.define_function_acceptable_password import is_acceptable_password


def test_is_acceptable_password():
    assert is_acceptable_password("short") is False
    assert is_acceptable_password("muchlonger") is False
    assert is_acceptable_password("ashort") is False
    assert is_acceptable_password("muchlonger5") is True
