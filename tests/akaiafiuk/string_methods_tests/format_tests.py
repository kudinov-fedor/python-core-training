import pytest


def test_format_using_indexes():
    """format string using named indexes"""
    test_string = "My name is {name}. I live in {city}".format(name="Anton", city="Kyiv")
    assert test_string == "My name is Anton. I live in Kyiv"


def test_format__using_pattern():
    """Format using string string pattern and passing dict as kwargs."""
    pattern = "My name is {name}. I live in {city}"
    data = dict(name="Anton", city="Kyiv")
    res = pattern.format(**data)
    assert res == "My name is Anton. I live in Kyiv"


def test_format_using_numbered_indexes():
    """format string using numbered indexes"""
    test_string = "My name is {0}. I live in {1}".format("Anton", "Kyiv")
    assert test_string == "My name is Anton. I live in Kyiv"


def test_format_using_empty_placeholders():
    """format string using empty placeholders"""
    test_string = "My name is {}. I live in {}".format("Anton", "Kyiv")
    assert test_string == "My name is Anton. I live in Kyiv"


def test_format_too_many_values():
    """format string using empty placeholders"""
    test_string = "My name is {}. I live in {}".format("Anton", "Kyiv", "outside range")
    assert test_string == "My name is Anton. I live in Kyiv"


def test_format_index_not_exist():
    """format string using empty placeholders"""
    with pytest.raises(IndexError, match="Replacement index 4 out of range for positional args tuple"):
        "My name is {1}. I live in {4}".format("Anton", "Kyiv", "outside range")
