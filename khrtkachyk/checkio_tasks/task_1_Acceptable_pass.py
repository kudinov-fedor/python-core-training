"""
In this mission, you need to create a password verification function.
The verification condition is:
- the length should be bigger than 6.
Input: A string (str).
Output: A logic value (bool).
"""


def is_acceptable_password(password: str) -> bool:
    return len(password.strip()) > 6


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password("short"))
    print(is_acceptable_password("ashort"))
    print(is_acceptable_password("muchlonger"))
