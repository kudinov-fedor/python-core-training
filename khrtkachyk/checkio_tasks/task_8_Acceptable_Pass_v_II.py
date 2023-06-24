"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit.
Input: A string (str).
Output: A logic value (bool).
"""


def is_acceptable_password(password: str) -> bool:
    valid_length = len(password.strip()) > 6
    contains_digits = any(i.isdigit() for i in password)
    return valid_length and contains_digits


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short14"))
    print(is_acceptable_password("muchlonger5"))
    print(is_acceptable_password("short1"))
    print(is_acceptable_password("lettersonly"))
