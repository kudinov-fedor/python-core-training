from typing import List, Any, Iterable


def unpack_recursive(lst: List[Any]) -> Iterable[Any]:
    for item in lst:
        if isinstance(item, list):
            yield from unpack_recursive(item)
        else:
            yield item


def test_unpack_recursive():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert list(unpack_recursive(target)) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
