from typing import List, Any, Iterable


def unpack_while_loop(lst: List[Any]):
    initial_queue = [lst]
    resulting = []
    while initial_queue:
        dequeue = initial_queue.pop()
        if isinstance(dequeue, (list, list)):
            for i in dequeue:
                initial_queue.append(i)
        else:
            resulting.append(dequeue)
    return resulting[::-1]


def test_unpack_while_loop():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
