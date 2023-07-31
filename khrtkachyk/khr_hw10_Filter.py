def my_filter(key, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """

    key = key or (lambda i: i)
    result = []
    for x in iterable:
        if key(x):
            result.append(x)
    return result


if __name__ == "__main__":
    a = [0, 1, 2, 0, 2, 3]

    assert list(filter(None, a)) == [1, 2, 2, 3]
    assert list(filter(lambda i: i < 2, a)) == [0, 1, 0]
    assert my_filter(None, a) == [1, 2, 2, 3]
    assert my_filter(lambda i: i < 2, a) == [0, 1, 0]
