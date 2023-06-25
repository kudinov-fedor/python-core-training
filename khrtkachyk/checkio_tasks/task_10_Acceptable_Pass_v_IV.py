"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit, but it cannot consist of just digits;
# if the password is longer than 9 - previous rule (about one digit), is not required.
Input: A string (str).
Output: A logic value (bool).
"""


def is_acceptable_password(password: str) -> bool:
    valid_length = len(password)
    contains_digits = any(i.isdigit() for i in password)
    contains_letters = any(i.isalpha() for i in password)
    if valid_length <= 6:
        return False
    if valid_length > 9:
        return True
    return contains_digits and contains_letters and not password.isdigit()


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short"))
    print(is_acceptable_password("short54"))
    print(is_acceptable_password("notshort"))
    print(is_acceptable_password("1234567899"))
    print(is_acceptable_password("muchlonger"))
    print(is_acceptable_password("-----------"))
