def unpack_while_loop(items):
    list_items = list(items)

    result = []
    while list_items:
        i = list_items.pop()
        if isinstance(i, (list, tuple)):
            list_items.extend(i)
        else:
            result.append(i)
    return result[::-1]


def unpack_recursive(items):
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(unpack_recursive(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":

    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
