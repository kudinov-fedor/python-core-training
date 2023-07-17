import pytest


def unpack_recursive(item):
    result = []
    for a in item:
        if isinstance(a, list):
            result.extend(unpack_recursive(a))
        else:
            result.append(a)
    return result


def test_unpack_recursive():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
