"""
***** Task6 *****
In this mission you need to create a password verification function.
*****************
The verification conditions are:
    the length should be bigger than 6;
    should contain at least one digit.
"""


def is_acceptable_password(password: str) -> bool:
    result = True if (len(password) > 6 and password.isalnum() and not password.isalpha()) else False
    return result


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
