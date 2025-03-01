import pytest


@pytest.mark.parametrize("string, ends_with, result", [
    ("HELLO!", "O!", True),         # True if a string ends with entered param
    ("123456", "6", True),          # Or a char
    ("123456", ("5", "6"), True),   # Or a tuple of strings
    ("123456", str(6), True),       # Can convert to string before passing param
    ("Hello", "There", False),      # False if does not end with the given param
    ("Hello", "HHello", False),     # Param is longer than the string itself
    ("HELLO", "lo", False),         # False since .endswith() is rank sensitive
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


@pytest.mark.parametrize("string, result", [
    ("1234567890", True),    # All characters are decimal
    ("123Abc", False),       # Not all are decimal characters
    ("\u0033", True),        # Unicode for 3
    ("\u00B2", False),       # Power of two ^2.
    ("\u00BD", False),       # ½
    ("ↁ", False),             # False for Roman numerals
])
def test_is_decimal(string, result):
    """Check if all the characters in the unicode object are decimals."""
    assert string.isdecimal() == result


@pytest.mark.parametrize("string, result", [
    ("1234567890", True),    # All characters are decimal digits
    ("\u0033", True),        # Unicode for 3
    ("\u00B2", True),        # Power of two ^2.
    ("ↁ", False),            # False for Roman numerals
    ("\u00BD", False),       # ½
    ("0.5", False),          # False for decimals
    ("1 5", False),          # False if contains spaces
])
def test_is_digit(string, result):
    """Check if all the characters in the text are digits."""
    assert string.isdigit() == result


@pytest.mark.parametrize("string, result", [
    ("1234567890", True),    # All characters are decimal
    ("\u0033", True),        # Unicode for 3
    ("\u00B2", True),        # Power of two ^2.
    ("\u00BD", True),        # ½
    ("ↁ", True),             # True for Roman numerals
    ("0.5", False),          # False for decimals
    ("1 5", False),          # False if contains spaces
    ("one", False),          # Not that smart though
])
def test_is_numeric(string, result):
    """Check if all the characters in the text are numeric."""
    assert string.isnumeric() == result


@pytest.mark.parametrize("string, result", [
    ("valid_identifier", True),     # Valid. Only letters and underscores
    ("Valid_1dent1f1er", True),     # Valid. Alphanumeric and underscores
    ("1nvalid_identifier", False),  # Invalid. Starts with number
    ("invalid identifier", False),  # Invalid. Contain spaces
    ("inv@lid identifier", False),  # Invalid. Contain @
])
def test_is_identifier(string, result):
    """
    isidentifier() method returns True if the string is a valid identifier, otherwise False.

    String is considered a valid identifier if it only contains alphanumeric letters, or underscores (_).
    A valid identifier cannot start with a number, or contain any spaces.
    """
    assert string.isidentifier() == result


@pytest.mark.parametrize("string, result", [
    ("all lower_1234567890!", True),     # all characters are lower
    ("a", True),                         # one letter in lower case
    ("hellO", False),                    # one capital letter. False
    (" 1234567890", False),              # no lowercase characters included. False

])
def test_is_lower(string, result):
    """
    islower() returns True when all characters are lowercase
    """
    assert string.islower() == result


@pytest.mark.parametrize("string, result", [
    ("ALL UPPER_1234567890!", True),
    ("A", True),
    ("Hello", False),
    (" 1234567890", False),

])
def test_is_upper(string, result):
    """
    isupper() returns True when all characters are uppercase
    """
    assert string.isupper() == result


@pytest.mark.parametrize("string, result", [
    ("Hello, World!", True),
    ("123 Questions", True),
    ("Hello 123!", True),
    ("HELLO WORLD", False),
    ("hello", False),
    (" 1234567890", False),

])
def test_is_title(string, result):
    """
    istitle() returns True when all words starts with an uppercase
    """
    assert string.istitle() == result


def test_is_printable():
    """Returns True if all characters are printable, False otherwise."""
    assert "ABC abc_123".isprintable()
    assert not "ABC abc_123\n".isprintable()


def test_is_space():
    """Returns True if all characters are whitespaces"""
    assert "     ".isspace()
    assert " ".isspace()
    assert not "hi there".isspace()
