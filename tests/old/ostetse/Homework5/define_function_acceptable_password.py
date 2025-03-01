import string


def is_acceptable_password(password: str) -> bool:
    has_no = set(password).isdisjoint
    return not (len(password) < 6 or has_no(string.digits))
