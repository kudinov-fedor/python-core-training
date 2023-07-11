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


def unpack_while_loop_generator(item):
    bunch = list(item)
    while bunch:
        par = bunch.pop()
        if isinstance(par, list):
            yield from unpack_while_loop_generator(par)
        else:
            yield par


def unpack_recursive(item):
    result = []

    for i in item:
        if isinstance(i, list):
            item.extend(unpack_recursive(list(i)))
        else:
            result.append(i)
    return result


def unpack_recursive_1(item):
    for i in item:
        if isinstance(i, list):
            yield from unpack_recursive_1(list(i))  # yiled all unpacked items one by one
        else:
            yield i


if __name__ == "__main__":
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive_1(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]


def test_my_gen():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    my_gen = unpack_recursive_1(target)
    gen_stack = []
    for i in my_gen:
        gen_stack.append(i)
    assert gen_stack == [123, "234", None, 1, 23, 123, 123, "sdf", True]


def test_unpack_while_gen():
    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    my_gen = unpack_while_loop_generator(target)
    gen_stack = []
    for i in my_gen:
        gen_stack.append(i)
    assert gen_stack[::-1] == [123, "234", None, 1, 23, 123, 123, "sdf", True]