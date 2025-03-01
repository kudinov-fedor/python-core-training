import re


def test_match_assertion():
    """Can just assert if there is a match by the given pattern."""
    result_match = re.search('[0-9][0-9][0-9]', 'foo987bar')
    result_no_match = re.search('[0-9][0-9][0-9]', 'foo98bar')
    assert result_match
    assert not result_no_match


def test_accessing_span():
    """Can get a tuple with match indexes from a re.Match object."""
    result = re.search('[0-9][0-9][0-9]', 'foo987bar123asd')
    assert result.span() == (3, 6)


def test_slice_from_match():
    """Get matched string using slice, start and end method from Match object."""
    sample_string = 'foo987bar123asd'
    result = re.search('[0-9][0-9][0-9]', sample_string)
    assert sample_string[result.start():result.end()] == '987'


def test_get_result_string_using_group():
    """Get matched string using group() method"""
    result = re.search('[0-9][0-9][0-9]', 'foo987bar123asd')
    assert result.group() == '987'
