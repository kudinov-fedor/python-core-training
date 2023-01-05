"""
In this mission you need to create a password verification function.

The verification conditions are:

the length should be bigger than 6;
should contain at least one digit.
"""
def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(map(str.isdigit, password))

    return all([cond1, cond2])


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")