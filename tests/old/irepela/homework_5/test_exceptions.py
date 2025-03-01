import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        5 / 0


def test_index_error():
    with pytest.raises(IndexError):
        a = []
        a[0]


def test_type_error():
    with pytest.raises(TypeError):
        1 + "123"


def test_attribute_error():
    with pytest.raises(AttributeError):
        a = []
        a.invalid


def test_syntax_error():
    with pytest.raises(SyntaxError):
        eval("x = ")
