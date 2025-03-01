def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') is False
    assert is_acceptable_password('much-longer') is True
    assert is_acceptable_password('ashort') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")
