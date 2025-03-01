import re


def test_dot_any_character():
    """The dot (.) metacharacter matches any character."""
    result = re.search('1...3', 'foo12a~3bar')
    assert result.span() == (3, 8)
    assert result.group() == '12a~3'


def test_dot_no_new_line():
    """The dot (.) metacharacter does not match a new line character."""
    result = re.search('1.3', 'foo1\n3bar')
    assert result is None


def test_brackets():
    """([]) represent a character class—an enumerated set of characters to match from."""
    result = re.search('3[abcd]', 'foo123bar')
    assert result.group() == '3b'


def test_brackets_char_range():
    """A character class can also contain a range of characters separated by a hyphen (-)"""
    result = re.search('3[a-c]a', 'foo123car')
    assert result.group() == '3ca'


def test_not_a_part_of_set():
    """^ as the first character, in which case it matches any character that isn’t in the set."""
    result = re.search('[^1-3]', '123car')
    assert result.group() == 'c'


def test_alphanumeric():
    """
    '\\w' matches any alphanumeric word character.
    Word characters are uppercase and lowercase letters, digits, and the underscore (_) character,
    so '\\w' is essentially shorthand for [a-zA-Z0-9_]
    """
    result = re.findall('\\w', '#(.a$@&B1_')
    assert result == ['a', 'B', '1', '_']


def test_non_alphanumeric():
    """
    \\W is the opposite. It matches any non-word character and is equivalent to [^a-zA-Z0-9_]:
    """
    result = re.search('\\W', 'abcd#(.a$@&')
    assert result.group() == '#'


def test_decimal():
    """\\d will seacrh for a decimal character"""
    result = re.search('\\d', '#(.abc1.2$@&')
    assert result.group() == '1'


def test_non_decimal():
    """\\D will seacrh for a non-decimal character"""
    result = re.search('\\D', '12$@&')
    assert result.group() == '$'


def test_space():
    """\\s will search for a space character"""
    result = re.search('\\s', '12 @&')
    assert result.group() == " "
    assert result.span() == (2, 3)


def test_not_a_space():
    """\\S will search for a character different from a space"""
    result = re.search('\\S', '  !@&')
    assert result.group() == '!'
