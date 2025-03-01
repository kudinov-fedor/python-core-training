"""
In this mission you need to create a password verification function.
The verification conditions are:
- the length should be bigger than 6;
- should contain at least one digit, but it cannot consist of just digits;
- having numbers or containing just numbers does not apply to the password longer than 9;
- a string should not contain the word "password" in any case.
Input: A string (str).
Output: A logic value (bool).
"""


def is_acceptable_password(password: str) -> bool:
    contains_substring = ("password" in password) or ("password".upper() in password)
    valid_length = 6 < len(password) <= 9
    too_short = len(password) <= 6
    at_least_one_digit = any(i.isdigit() for i in password)
    not_only_digits = any(i.isalpha() for i in password)
    is_long_password = len(password) > 9
    valid_short = not too_short and at_least_one_digit and (not contains_substring) and not_only_digits
    valid_long = is_long_password and (not contains_substring)
    just_valid_length = valid_length and (not contains_substring) and not_only_digits and at_least_one_digit
    pass_is_valid = just_valid_length or valid_long or valid_short
    return pass_is_valid


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short"))
    print(is_acceptable_password("short54")) #True
    print(is_acceptable_password("muchlonger")) #True
    print(is_acceptable_password("ashort"))
    print(is_acceptable_password("muchlonger5")) #True
    print(is_acceptable_password("sh5"))
    print(is_acceptable_password("1234567"))
    print(is_acceptable_password("12345678910")) #True
    print(is_acceptable_password("password12345"))
    print(is_acceptable_password("PASSWORD12345"))
    print(is_acceptable_password("pass1234word")) #True
