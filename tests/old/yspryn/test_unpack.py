from yspryn.hw6.unpack import unpack_while_loop, unpack_recursive

target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]


def test_unpack_while_loop():
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_while_loop([1, 2, 3]) == [1, 2, 3]


def test_unpack_recursive():
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive([1, 2, 3]) == [1, 2, 3]
