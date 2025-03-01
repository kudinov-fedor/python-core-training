"""
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit.
"""
def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(map(str.isdigit, password))

    return all([cond1, cond2])