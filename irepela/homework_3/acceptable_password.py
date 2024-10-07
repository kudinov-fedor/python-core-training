def check_password(password: str) -> bool:
    """
        Checks if password meets verifications conditions

        Args:
            password (str): password to check

        Returns:
            bool: result if password meets requirements
    """

    contains_pass = password == "password"
    complies_to_digit_policy = any(char.isdigit() for char in password) and not password.isnumeric()

    is_valid_short = len(password) > 6 and complies_to_digit_policy and not contains_pass
    is_valid_long = len(password) > 9 and not contains_pass

    return is_valid_short or is_valid_long
