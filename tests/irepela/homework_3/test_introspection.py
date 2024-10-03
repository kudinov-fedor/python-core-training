import pytest
from irepela.homework_3.introspection import check_default_bool, check_bool_instance


@pytest.mark.parametrize("expected", [
    False
])
def test_convert_binary_to_decimal(expected):
    assert check_default_bool() == expected


@pytest.mark.parametrize("a, expected", [
    (int, True),
    (float, False),
])
def test_check_bool_instance(a, expected):
    assert check_bool_instance(a) == expected
