"""
In this mission, you need to create a password verification function.

The verification condition is:

the length should be bigger than 6.
Input: A string.

Output: A bool.
"""


def is_acceptable_password(password: str):
    return len(password) > 6
