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
