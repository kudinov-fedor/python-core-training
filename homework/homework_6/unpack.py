
def unpack_while_loop(item):

    return []


def unpack_recursive(item):
    return []



if __name__ == "__main__":

    target = [123, ["234", None], [[1], [23], [[123], 123, ["sdf", True]]]]
    assert unpack_while_loop(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
    assert unpack_recursive(target) == [123, "234", None, 1, 23, 123, 123, "sdf", True]
