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
    too_short = len(password) <= 6
    at_least_one_digit = any(i.isdigit() for i in password)
    all_digits = all(i.isdigit() for i in password)
    not_only_digits = any(i.isalpha() for i in password)
    is_long_password = len(password) > 9

    valid_short = not too_short and at_least_one_digit and not_only_digits
    valid_long = is_long_password and (not_only_digits or all_digits)
    just_valid_length = valid_length and not_only_digits and at_least_one_digit

    pass_is_valid = just_valid_length or valid_long or valid_short
    return pass_is_valid


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("sh5"))
    print(is_acceptable_password("1234567"))
    print(is_acceptable_password("short"))
    print(is_acceptable_password("short54"))
    print(is_acceptable_password("notshort"))
    print(is_acceptable_password("1234567899"))
    print(is_acceptable_password("muchlonger"))
    print(is_acceptable_password("-----------"))
    print(is_acceptable_password("-------"))
