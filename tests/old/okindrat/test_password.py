# you need to create a password verification function.The verification condition is:
# the length should be bigger than 6


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


def test_accaptablepassword():

    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
