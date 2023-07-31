def my_enumerate(iterable, start=0):
    """
    Return an enumerate object.

      iterable
        an object supporting iteration

    Enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.

    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    """

    count = start
    for val in iterable:
        yield count, val
        count += 1


if __name__ == "__main__":
    a = ["a", "b", "c"]
    b = ["x", "y", "z"]
    print(list(my_enumerate(a)))
    print(list(my_enumerate(b)))

    assert list(enumerate(a)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(enumerate(a, start=2)) == [(2, "a"), (3, "b"), (4, "c")]
    assert list(my_enumerate(a)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(my_enumerate(a, start=2)) == [(2, "a"), (3, "b"), (4, "c")]
