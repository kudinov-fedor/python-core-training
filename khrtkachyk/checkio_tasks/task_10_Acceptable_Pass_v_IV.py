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
    is_not_digit = all(i.isdigit() for i in password)
    return (valid_length > 6 and contains_digits) and not is_not_digit or valid_length > 9


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short"))
    print(is_acceptable_password("short54"))
    print(is_acceptable_password("notshort"))
    print(is_acceptable_password("1234567899"))
    print(is_acceptable_password("muchlonger"))
    print(is_acceptable_password("-----------"))
    print(is_acceptable_password("-------"))
