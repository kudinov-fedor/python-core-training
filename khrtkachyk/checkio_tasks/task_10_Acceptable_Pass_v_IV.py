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
    valid_length = 6 < len(password) <= 9
    not_too_short = len(password) <= 6
    at_least_one_digit = any(i.isdigit() for i in password)
    not_only_digits = any(i.isalpha() for i in password)
    is_long_password = len(password) > 9

    just_valid_length = valid_length and at_least_one_digit and not_only_digits
    valid_short = not not_too_short and at_least_one_digit and not_only_digits
    valid_long = is_long_password and not_only_digits

    pass_is_valid = valid_long or valid_short or just_valid_length
    return pass_is_valid


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short"))
    print(is_acceptable_password("short54"))
    print(is_acceptable_password("notshort"))
    print(is_acceptable_password("1234567899"))
    print(is_acceptable_password("muchlonger"))
    print(is_acceptable_password("-----------"))
    print(is_acceptable_password("-------"))
