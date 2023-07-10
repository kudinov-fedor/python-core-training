import pytest


def min(*args, key=None):
    key = key or (lambda a: a)
    value, *args = args

    for a in args:
        if key(a) < key(value):
            value = a
    assert isinstance(value, object)
    return value


def test_min():
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6) == -7
    assert min(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == 1


def max(*args, key=None):
    key = key or (lambda a: a)
    value, *args = args

    for a in args:
        if key(a) > key(value):
            value = a
    assert isinstance(value, object)
    return value


def test_max():
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6
    assert max(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 6


def sorted(*args, key=None, reverse=False):
    """
    Ascending by default
    """
    expected = []
    if reverse:
        func = max
    else:
        func = min

    assert args
    args = list(args)
    while args:
        item = func(*args, key=key)
        args.remove(item)
        expected.append(item)
    return expected


def test_sorted():
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6) == [-7, -4, -2, 1, 2, 3, 4, 5, 6]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, reverse=True) == [6, 5, 4, 3, 2, 1, -2, -4, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs) == [1, -2, 2, 3, -4, 4, 5, 6, -7]
    assert sorted(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=abs, reverse=True) == [-7, 6, 5, -4, 4, 3, -2, 2, 1]
