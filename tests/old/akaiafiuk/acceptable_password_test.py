from akaiafiuk.acceptable_password import is_acceptable_password


def test_is_acceptable_password():
    assert not is_acceptable_password('short')
    assert is_acceptable_password('muchlonger')
    assert not is_acceptable_password('ashort')
