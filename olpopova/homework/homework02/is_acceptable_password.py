"""
**********************************************************************
In this mission you need to create a password verification function.

The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit.
**********************************************************************
"""


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and password.isalnum() and not password.isalpha()


"""
**********************************************************************
4th edition:

The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    if the password is longer than 9 - previous rule (about one digit), is not required.
**********************************************************************
"""


def is_acceptable_password_4th_edition(password: str) -> bool:
    # intermediate steps
    is_short_pass = 6 < len(password) < 9
    short_pass_checks = password.isalnum() and not password.isalpha() and not password.isdecimal()
    is_long_pass = len(password) > 9
    long_pass_checks = password.isalnum()

    return is_short_pass and short_pass_checks or is_long_pass and long_pass_checks


"""
**********************************************************************
5th edition:

The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9;
    # it means that long password could be isdecimal, isalpha or isalnum
    a string should not contain the word "password" in any case.
**********************************************************************
"""


def is_acceptable_password_5th_edition(password: str) -> bool:
    # intermediate steps
    is_short_pass = 6 < len(password) < 9
    is_digit_exist = any((i.isdigit() for i in password))
    short_pass_checks = all([is_digit_exist, not password.isdigit()])
    is_long_pass = len(password) > 9
    long_pass_checks = all([password.isalnum(), 'password' not in password.lower()])

    return is_short_pass and short_pass_checks or is_long_pass and long_pass_checks


"""
6th edition:

The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case;
    should contain at least 3 different (case-sensitive) letters (or digits) even if it is longer than 10
"""


def is_acceptable_password_6th_edition(password: str) -> bool:
    # intermediate steps
    is_short_pass = 6 < len(password) < 9
    is_digit_exist = any((i.isdigit() for i in password))
    is_case_sensitive = len(set(password)) >= 3
    short_pass_checks = all([is_digit_exist, not password.isdigit(), is_case_sensitive])
    is_long_pass = len(password) >= 9
    long_pass_checks = all([password.isalnum(), 'password' not in password.lower(), is_case_sensitive])

    return is_short_pass and short_pass_checks or is_long_pass and long_pass_checks
