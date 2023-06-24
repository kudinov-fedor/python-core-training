"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit.
Input: A string (str).
Output: A logic value (bool).
"""


def is_acceptable_password(password: str) -> bool:
    return True if len(password.strip()) > 6 and any(i.isdigit() for i in password) else False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short14"))
    print(is_acceptable_password("muchlonger5"))
    print(is_acceptable_password("short1"))
