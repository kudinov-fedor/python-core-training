
def unpack_while_loop(item):
    queue = list(item)

    res = []
    while queue:
        i = queue.pop()
        if isinstance(i, (list, tuple)):
            queue.extend(i)
        else:
            res.append(i)
    return res[::-1]


def unpack_while_loop_gen(item):
    queue = list(item)

    while queue:
        i = queue.pop(0)
        if isinstance(i, (list, tuple)):
            queue = i + queue
        else:
            yield i


def unpack_recursive(item):
    res = []
    for i in item:
        if isinstance(i, (list, tuple)):
            res.extend(unpack_recursive(i))
        else:
            res.append(i)
    return res


def unpack_recursive_gen(item):
    for i in item:
        if isinstance(i, (list, tuple)):
            yield from unpack_recursive(i)
        else:
            yield i


if __name__ == "__main__":

    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert list(unpack_while_loop_gen(target)) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert list(unpack_recursive_gen(target)) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
