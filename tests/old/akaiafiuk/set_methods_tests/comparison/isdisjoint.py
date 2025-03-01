import pytest


def test_isdisjoint_positive():
    """isdisjoint() returns False if sets has common elements"""
    x = {1, 2, 3}
    y = {3, 4, 5, 6}
    assert x.isdisjoint(y) is False


def test_isdisjoint_negative():
    """isdisjoint() returns True if sets does not have common elements"""
    x = {1, 2, 3}
    y = {4, 5, 6}
    assert x.isdisjoint(y)


def test_isdisjoint_multiple_sets():
    """isdisjoint() accepts only one argument"""
    x = {1, 2, 3}
    y = {4, 5, 6}
    z = {7, 8, 9}
    with pytest.raises(TypeError):
        x.isdisjoint(y, z)


def test_isdisjoint_dict():
    """isdisjoint() can accept dict as an argument. In such case it works with keys."""
    x = {1, 2, 3}
    y = {4: 'a', 5: 'b', 6: 'c'}
    assert x.isdisjoint(y)


def test_isdisjoint_list():
    """isdisjoint() can accept any iterable as an argument."""
    x = {1, 2, 3}
    y = [4, 5, 6, 6]
    assert x.isdisjoint(y)
