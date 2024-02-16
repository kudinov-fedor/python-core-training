from nataliia_romanchuk.homework6.unpack import unpack_recursive, unpack_while_loop
import pytest

@pytest.mark.parametrize("some_item", [[123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]])
def test_unpack_while_loop(some_item):
    assert unpack_while_loop(some_item) == [123, "234", None, 1, 23, 123, 123, "sdf", True]

@pytest.mark.parametrize("some_item", [[123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]])
def test_unpack_recursive(some_item):
    assert unpack_recursive(some_item) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
