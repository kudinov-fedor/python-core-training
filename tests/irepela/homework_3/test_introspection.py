import pytest
from irepela.homework_3.introspection import get_default_bool, check_bool_instance, check_bool_subclass


def test_convert_binary_to_decimal():
    assert get_default_bool() is False


@pytest.mark.parametrize("a, expected", [
    (int, True),
    (float, False),
])
def test_check_bool_instance(a, expected):
    assert check_bool_instance(a) == expected


@pytest.mark.parametrize("a, expected", [
    (int, True),
    (float, False),
])
def test_check_bool_subclass(a, expected):
    assert check_bool_subclass(a) == expected
