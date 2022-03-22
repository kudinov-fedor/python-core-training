"""You are at the beginning of a password series. Every mission is based on the previous one.
The missions that follow will become slightly more complex.

In this mission, you need to create a password verification function.

The verification condition is:

the length should be bigger than 6.
Input: A string.

Output: A bool."""


def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False
