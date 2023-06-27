def is_acceptable_password(password: str) -> bool:
    if "password" in password.lower():
        return False
    elif (any(char.isdigit() for char in password) and len(password) >= 6 and not password.isnumeric()) or len(password) >= 9:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short"))

    # These "asserts" are used for self-checking
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True

    print("The mission is done! Click 'Check Solution' to earn rewards!")
