import pytest


def test_format_int_old():
    """Old school way of formatting int"""
    assert "Int %d" % (42,) == "Int 42"


def test_format_int():
    """Formatting int using format() method"""
    assert "Int {:d}".format(42) == "Int 42"


def test_format_int_literal():
    """Formatting int using format() method"""
    assert f"Int {42:d}" == "Int 42"


def test_fail_if_not_int():
    """Error occurs if passing not an integer"""
    with pytest.raises(ValueError, match="Unknown format code 'd' for object of type 'float'"):
        f"Int {42.1:d}"


def test_format_float_old():
    """Old school way of formatting float"""
    assert 'Float: %f' % (3.141592653589793,) == "Float: 3.141593"


def test_format_float():
    """Old school way of formatting float"""
    assert 'Float: {:f}'.format(3.141592653589793) == "Float: 3.141593"


def test_format_float_literal():
    """Old school way of formatting float"""
    assert f'Float: {3.141592653589793:f}' == "Float: 3.141593"
