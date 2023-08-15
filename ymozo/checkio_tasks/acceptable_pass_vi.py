def is_acceptable_password(password: str) -> bool:
    long_pass = len(password) >= 9
    enough_length = len(password) >= 6
    at_least_one_digit = any(char.isdigit() for char in password)
    not_only_digits = not password.isnumeric()
    pass_word = "password" not in password.lower()

    pass_list = set(password)
    char_count = []
    for char in pass_list:
        char_count.append(char)

    unique_char_count = len(char_count)

    valid_pass = enough_length and at_least_one_digit and not_only_digits and pass_word
    valid_pass_long = long_pass and pass_word

    return (valid_pass or valid_pass_long) and unique_char_count >= 3


if __name__ == "__main__":
    print("Example:")
    print(is_acceptable_password("short"))

    # These "asserts" are used for self-checking
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("short54") == True
    assert is_acceptable_password("muchlonger") == True
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    assert is_acceptable_password("1234567") == False
    assert is_acceptable_password("12345678910") == True
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    assert is_acceptable_password("aaaaaa1") == False
    assert is_acceptable_password("aaaaaabbbbb") == False
    assert is_acceptable_password("aaaaaabb1") == True
    assert is_acceptable_password("abc1") == False
    assert is_acceptable_password("abbcc12") == True
    assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")