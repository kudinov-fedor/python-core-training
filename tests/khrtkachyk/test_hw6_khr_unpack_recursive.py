from typing import List, Any, Iterable


def unpack_recursive(lst: List[Any]) -> Iterable[Any]:
    for sublist in lst:
        if isinstance(sublist, list):
            yield from unpack_recursive(sublist)
        else:
            yield sublist


def test_unpack_recursive():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert list(unpack_recursive(target)) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
