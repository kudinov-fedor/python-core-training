import pytest


def unpack_while_loop(item):
    result = []
    given = list(item)
    while given:
        item = given.pop()
        if isinstance(item, list):
            given.extend(item)
        else:
            result.append(item)
    return result[::-1]


def test_unpack_while_loop():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
