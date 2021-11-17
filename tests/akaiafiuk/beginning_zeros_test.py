import pytest
from akaiafiuk.beginning_zeros import beginning_zeros, beginning_zeros_using_split


@pytest.mark.parametrize("foo", [
    beginning_zeros,
    beginning_zeros_using_split
])
@pytest.mark.parametrize("input_value, expected_result", [
    ("100", 0),
    ("001", 2),
    ("100100", 0),
    ("001001", 2),
    ("012345679", 1),
    ("0000", 4)
])
def test_beginning_zeros_functions(foo, input_value, expected_result):
    assert foo(input_value) == expected_result
