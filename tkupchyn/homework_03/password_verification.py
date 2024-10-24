def is_acceptable_password(password: str) -> bool:
    """
    Function verify is given conditions are met:
    - the length should be bigger than 6;
    - should contain at least one digit, but it cannot consist of just digits;
    - having numbers or containing just numbers does not apply to the password longer than 9;
    - a string should not contain the word "password" in any case.

    Args:
         password (str): The input string that may contain a mixture of digits and letters.

    Returns:
        bool: True if password is acceptable, False otherwise.
    """
    if len(password) < 7:
        return False

    if 'password' in password:
        return False

    if len(password) <= 9:
        if all(symbol.isdigit() for symbol in password) or not any(symbol.isdigit() for symbol in password):
            return False

    return True


def is_acceptable_password_alternative(password: str) -> bool:

    is_short = len(password) < 7
    has_pass = 'password' in password
    has_only_digits = all(symbol.isdigit() for symbol in password)
    has_digits = any(symbol.isdigit() for symbol in password)

    valid_long = len(password) > 9 and not has_pass
    valid_short = all([not is_short, not has_pass, not has_only_digits, has_digits])

    return valid_long or valid_short
