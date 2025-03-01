from nataliia_romanchuk.homework6.unpack import unpack_recursive, unpack_while_loop
import pytest

@pytest.mark.parametrize("func", [unpack_while_loop, unpack_recursive])
def test_unpack(func):
    some_item = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert func(some_item) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    
