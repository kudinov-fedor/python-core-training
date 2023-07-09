def unpack_while_loop(item):
    result = []

    bunch = list(item)
    while bunch:
        item = bunch.pop()
        if isinstance(item, list):
            bunch.extend(item)
        else:
            result.append(item)
    return result[::-1]


def unpack_recursive(item):
    result = []

    for i in item:
        if isinstance(i, list):
            item.extend(i)
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
