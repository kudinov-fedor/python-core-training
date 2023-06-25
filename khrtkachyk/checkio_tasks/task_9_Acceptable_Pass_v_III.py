"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit, but cannot consist of just digits.

Input: A string (str).
Output: A logic value (bool).
"""


def is_acceptable_password(password: str) -> bool:
    valid_length = len(password.strip()) > 6
    contains_digits = any(i.isdigit() for i in password)
    contains_letters = any(i.isalpha() for i in password)
    contains_spec_chars = any(i.isalnum() for i in password)
    return valid_length and contains_digits and contains_letters and contains_spec_chars


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("k"))
    print(is_acceptable_password("1234567a"))
    print(is_acceptable_password("acceptable6_"))
    print(is_acceptable_password("letteranddigit1*"))
