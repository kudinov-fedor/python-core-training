import pytest
from irepela.homework_6.unpack import unpack_while_loop, unpack_recursive


@pytest.mark.parametrize("a, expected", [
    ([123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]],
     [123, "234", None, 1, 23, 123, 123, "sdf", True])
])
def test_unpack_while_loop(a, expected):
    assert unpack_while_loop(a) == expected


@pytest.mark.parametrize("a, expected", [
    ([123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]],
     [123, "234", None, 1, 23, 123, 123, "sdf", True])
])
def test_unpack_recursive(a, expected):
    assert unpack_recursive(a) == expected
