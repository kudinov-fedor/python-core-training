from khr_hw10_Recreate_ZIP import my_zip


def my_map(func, *iterables):
    """
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """

    iter_obj = [iter(i) for i in iterables]
    try:
        while True:
            func_param = [next(j) for j in iter_obj]
            yield func(*func_param)
    except StopIteration:
        return


def my_map_2(func, *iterables):
    for item in my_zip(*iterables):
        yield func(*item)


if __name__ == "__main__":

    a = [0, 1, 2, 0, 2, 3]
    b = [3, 1, 2, 2, 1, 4]
    add = (lambda a, b: a + b)

    # asserts for builtin "map()"
    assert list(map(str, a)) == ["0", "1", "2", "0", "2", "3"]
    assert list(map(add, a, b)) == [3, 2, 4, 2, 3, 7]

    # asserts for "my_map()"
    assert list(my_map(str, a)) == ["0", "1", "2", "0", "2", "3"]
    assert list(my_map(add, a, b)) == [3, 2, 4, 2, 3, 7]

    # asserts for "my_map_2()"
    assert list(my_map_2(str, a)) == ["0", "1", "2", "0", "2", "3"]
    assert list(my_map_2(add, a, b)) == [3, 2, 4, 2, 3, 7]
