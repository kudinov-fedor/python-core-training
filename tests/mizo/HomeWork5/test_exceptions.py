import pytest


def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        5 / 0


def test_type_error():
    with pytest.raises(TypeError):
        1 + "123"
