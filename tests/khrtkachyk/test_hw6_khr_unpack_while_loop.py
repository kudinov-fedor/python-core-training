from typing import List, Any


def unpack_while_loop(lst: List[Any]):
    initial_queue = [lst]
    while initial_queue:
        dequeue = initial_queue.pop(0)
        if isinstance(dequeue, list):
            initial_queue = dequeue + initial_queue
        else:
            yield dequeue


def test_unpack_while_loop():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert list(unpack_while_loop(target)) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
