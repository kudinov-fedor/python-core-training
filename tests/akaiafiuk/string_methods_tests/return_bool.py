import pytest


@pytest.mark.parametrize("string, ends_with, result", [
    ("HELLO!", "O!", True),         # True if a string ends with entered param
    ("123456", "6", True),          # Or a char
    ("123456", ("5", "6"), True),   # Or a tuple of strings
    ("123456", str(6), True),       # Can convert to string before passing param
    ("Hello", "There", False),      # False if does not end with the given param
    ("Hello", "HHello", False),     # Param is longer than the string itself
])
def test_endswith(string, ends_with, result):
    """Verify that a string ends with entered parameter and returns bool."""
    assert string.endswith(ends_with) == result


def test_endswith_start_stop():
    """.endswith() can receive start and stop as arguments"""
    assert "Hello".endswith("lo", 1, 5)      # Just to demo. End index is outside of the range
    assert not "Hello".endswith("lo", 1, 4)  # Stop index is not included so expecting False here


@pytest.mark.parametrize("string, ends_with", [
    ("123456", 6),
    ("123456", ["6"]),
])
def test_endswith_negative(string, ends_with):
    """Verify that value error is thrown when passing not a string."""
    with pytest.raises(TypeError, match="endswith first arg must be str or a tuple of str"):
        string.endswith(ends_with)


@pytest.mark.parametrize("string, result", [
    ("1234567890", True),
    ("123456a", True),
    ("HelloWorld", True),
    ("Hello World", False),
    ("123-456-789-0", False),
    ("123 45678 90", False),
])
def test_is_all_num(string, result):
    """.isalnum() returns True if all characters are alphanumeric, False otherwise."""
    assert string.isalnum() == result


@pytest.mark.parametrize("string, result", [
    ("HelloWorld", True),    # All characters are alphanumeric
    ("123456a", False),      # Some characters are numbers
    ("Hello World", False),  # Space included
    ("Hello-World", False),  # Dash is also not an alpha
])
def test_is_alpha(string, result):
    """.isalpha() returns True if all characters are letters, False otherwise."""
    assert string.isalpha() == result


def test_is_ascii():
    """
    Verify if all characters in the string are ascii characters

    ASCII is a 7-bit character set containing 128 characters.
    It contains the numbers from 0-9, the upper and lower case English letters from A to Z, and some special characters.
    """
    assert "Hello World 1234567890 !".isascii()
    assert not "日本人 中國的".isascii()
