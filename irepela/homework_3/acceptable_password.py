def check_password(password: str) -> bool:
    """
        Checks if password meets verifications conditions

        Args:
            password (str): password to check

        Returns:
            bool: result if password meets requirements
    """

    is_valid_password = len(password) > 6 and password != "password"
    if is_valid_password and len(password) < 9:
        is_valid_password = not password.isalpha() and not password.isnumeric()

    return is_valid_password
