"""
You are at the beginning of a password series. Every mission is based on the previous one. The missions that follow will become slightly more complex.

In this mission, you need to create a password verification function.

The verification condition is:

the length should be bigger than 6.
"""
def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) >9
