from dyurchen.acceptable_pass import is_acceptable_password


def test_is_acceptable_password():
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('muchlonger') is True
    assert is_acceptable_password('ashort') is False
