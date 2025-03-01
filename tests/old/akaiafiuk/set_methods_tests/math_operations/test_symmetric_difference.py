import pytest

a = {1, 2, 3}
b = {3, 4, 5}
c = {6, 7, 8}


def test_symmetric_difference_method():
    """Symmetric difference using method removes common elements"""
    x = a.symmetric_difference(b)
    assert a == {1, 2, 3}
    assert x == {1, 2, 4, 5}


def test_symmetric_difference_method_not_set():
    """Symmetric difference argument will be transformed to set"""
    x = a.symmetric_difference([3, 3, 3, 4, 5, 5])
    assert x == {1, 2, 4, 5}


def test_symmetric_difference_multiple_arguments():
    """symmetric_difference() method accept only one argument"""
    with pytest.raises(TypeError):
        a.symmetric_difference([3, 3, 5], [3, 4, 5, 5])


def test_symmetric_difference_operator():
    """^ operator stands for symmetric difference"""
    x = a ^ b
    assert a == {1, 2, 3}
    assert x == {1, 2, 4, 5}


def test_symmetric_difference_update_method():
    """symmetric_difference_update updates the set in place."""
    a.symmetric_difference_update(b)
    assert a == {1, 2, 4, 5}


def test_symmetric_difference_in_place_operator():
    """symmetric_difference_update updates the set in place and can work with multiple arguments"""
    one = {1, 2, 3}
    two = {3, 4, 5}
    one ^= two
    assert one == {1, 2, 4, 5}
