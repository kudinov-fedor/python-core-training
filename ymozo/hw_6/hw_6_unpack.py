def unpack_while_loop(item):
    result = []

    bunch = list(item)
    while bunch:
        par = bunch.pop()
        if isinstance(par, list):
            bunch.extend(par)
        else:
            result.append(par)
    return result[::-1]

    # result = []
    # bunch = list(item)
    # while bunch:
    #     par = bunch.pop()
    #     if isinstance(par, list):
    #         bunch.extend(par)
    #     else:
    #         result.append(par)
    # yield from result[::-1]
    #
    # generator = unpack_while_loop(item)
    # for i in generator:
    #     return i


def unpack_recursive(item):
    result = []

    for i in item:
        if isinstance(i, list):
            item.extend(unpack_recursive(list(i)))
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
