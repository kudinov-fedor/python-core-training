import pytest


def error_func():
    a = lambda: 123
    a(1, 2, 3)


def test_type_error1_0():
    with pytest.raises(TypeError):
        error_func()


def test_type_error2_0():
    with pytest.raises(TypeError) as excinfo:
        error_func()
    assert "positional arguments" in str(excinfo.value)


def test_type_error3_0():
    with pytest.raises(BaseException):
        error_func()
