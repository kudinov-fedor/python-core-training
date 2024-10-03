import pytest
from irepela.homework_3.conversion import (convert_binary_to_decimal, convert_to_list,
                                           convert_to_tuple, convert_to_set)


@pytest.mark.parametrize("a, expected", [
    ("10110101", 181),
    ("0b10110101", 181),
])
def test_convert_binary_to_decimal(a, expected):
    assert convert_binary_to_decimal(a) == expected


@pytest.mark.parametrize("a, expected", [
    ({"a": 1, "b": 2}, ["a", "b"]),
    ({"a", "b"}, ["a", "b"]),
])
def test_convert_to_list(a, expected):
    assert convert_to_list(a) == expected


@pytest.mark.parametrize("a, expected", [
    ({"a": 1, "b": 2}, ("a", "b")),
    ({"a", "b"}, ("a", "b")),
])
def test_convert_to_tuple(a, expected):
    assert convert_to_tuple(a) == expected


@pytest.mark.parametrize("a, expected", [
    ("abc", {"a", "b", "c"}),
    ({"a": 1, "b": 2}, {"a", "b"})
])
def test_convert_to_set(a, expected):
    assert convert_to_set(a) == expected
