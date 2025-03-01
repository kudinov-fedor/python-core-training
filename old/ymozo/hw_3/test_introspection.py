import pytest


def test_some_int():
    some_int = int()
    assert some_int == 0


def test_some_list():
    some_list = list()
    assert some_list == []


def test_zero_division_exception():
    try:
        10 / 0
    except ZeroDivisionError as error:
        assert isinstance(error, ZeroDivisionError)


@pytest.mark.parametrize(["param", "result"], [
    (isinstance(bool, type), True),
    (isinstance(bool, object), True),
    (issubclass(bool, bool), True),
    (issubclass(bool, int), True),
    (issubclass(bool, float), False),
    (issubclass(ZeroDivisionError, ArithmeticError), True),
    (issubclass(ZeroDivisionError, Exception), True)
])
def test_is_inst_subclass(param, result):
    assert param == result