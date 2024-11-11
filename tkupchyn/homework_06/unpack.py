def unpack_while_loop(item):
    sequence = list(item)
    result = []
    while sequence:
        elem = sequence.pop(0)
        if isinstance(elem, (tuple, list)):
            sequence.extend(elem)
        else:
            result.append(elem)
    return result


def unpack_recursive(item):
    sequence = []
    for element in item:
        if isinstance(element, (tuple, list)):
            sequence.extend(unpack_recursive(element))
        else:
            sequence.append(element)
    return sequence


if __name__ == "__main__":
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, '234', None, 1, 23, 123, 123, 'sdf', True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
