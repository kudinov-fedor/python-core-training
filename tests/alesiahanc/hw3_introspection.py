import pytest


class MyZeroError:
    try:
        1 / 0
    except ZeroDivisionError as zero_div_error:
        zero_error = zero_div_error


my_instance = MyZeroError()


@pytest.mark.parametrize(['arg', 'expected_type'], [
    (True, (int, float, str)),
    (True, object),
    (my_instance, MyZeroError),
    (MyZeroError.zero_error, ZeroDivisionError),
    (bool, type),
    (bool, object)

])
def test_get_type(arg, expected_type):
    assert isinstance(arg, expected_type)


@pytest.mark.parametrize(['arg', 'expected_class'], [
    (ZeroDivisionError, ArithmeticError),
    (ZeroDivisionError, Exception)
])
def test_is_subclass(arg, expected_class):
    assert issubclass(arg, expected_class)


@pytest.mark.parametrize(['arg', 'expected'], [
    ([], "append"),
    (int, "bool")
])
def test_has_attribute(arg, expected):
    assert hasattr(arg, expected)
