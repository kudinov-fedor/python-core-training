from typing import List, Any


def unpack_while_loop(lst: List[Any]):
    initial_queue = [lst]
    resulting = []
    while initial_queue:
        dequeue = initial_queue.pop(0)
        if isinstance(dequeue, list):
            for i in dequeue:
                initial_queue.insert(0, i)
        else:
            resulting.insert(0, dequeue)
    yield resulting


def test_unpack_while_loop():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    for value in unpack_while_loop(lst=target):
        assert value == [123, "234", None, 1, 23, 123, 123, "sdf", True]
