"""
***** Task6 **********************************************************
In this mission you need to create a password verification function.

The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit.
**********************************************************************
4th edition:

The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    if the password is longer than 9 - previous rule (about one digit), is not required.
**********************************************************************
5th edition:

The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9;
    a string should not contain the word "password" in any case.
**********************************************************************
"""


def is_acceptable_password(password: str) -> bool:
    result = True if (len(password) > 6 and password.isalnum() and not password.isalpha()) else False
    return result


# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False


def is_acceptable_password_4th_edition(password: str) -> bool:
    result = False
    if 6 < len(password) < 9:
        result = password.isalnum() and not password.isalpha() and not password.isdecimal()
    elif len(password) > 9:
        result = password.isalnum() or " " in password
    return result


# These "asserts" are used for self-checking
assert is_acceptable_password_4th_edition("short") == False
assert is_acceptable_password_4th_edition("short54") == True
assert is_acceptable_password_4th_edition("muchlonger") == True
assert is_acceptable_password_4th_edition("ashort") == False
assert is_acceptable_password_4th_edition("notshort") == False
assert is_acceptable_password_4th_edition("muchlonger5") == True
assert is_acceptable_password_4th_edition("sh5") == False
assert is_acceptable_password_4th_edition("1234567") == False
assert is_acceptable_password_4th_edition("12345678910") == True
assert is_acceptable_password_4th_edition('this is password') == True


def is_acceptable_password_5th_edition(password: str) -> bool:
    result = False
    if 6 < len(password) < 9:
        result = password.isalnum() and not password.isalpha() and not password.isdecimal()
    elif len(password) > 9 and ('password' not in password.lower()):
        result = password.isalnum() or " " in password
    return result


# These "asserts" are used for self-checking
assert is_acceptable_password_5th_edition("short") == False
assert is_acceptable_password_5th_edition("short54") == True
assert is_acceptable_password_5th_edition("muchlonger") == True
assert is_acceptable_password_5th_edition("ashort") == False
assert is_acceptable_password_5th_edition("muchlonger5") == True
assert is_acceptable_password_5th_edition("sh5") == False
assert is_acceptable_password_5th_edition("1234567") == False
assert is_acceptable_password_5th_edition("12345678910") == True
assert is_acceptable_password_5th_edition("password12345") == False
assert is_acceptable_password_5th_edition("PASSWORD12345") == False
assert is_acceptable_password_5th_edition("pass1234word") == True
