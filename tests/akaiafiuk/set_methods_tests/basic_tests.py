from collections import Hashable

import pytest


def test_creation_literal():
    """Set can be created by literal"""
    test_set = {'banana', 'apple', 'orange', 'orange'}
    assert isinstance(test_set, set)
    assert len(test_set) == 3
    assert test_set == {'banana', 'apple', 'orange'}


def test_create_using_method():
    """Set can be created using special method"""
    test_set = set(['banana', 'apple', 'orange', 'orange'])
    assert isinstance(test_set, set)
    assert len(test_set) == 3
    assert test_set == {'banana', 'apple', 'orange'}


def test_create_empty_set():
    """Empty set can be created only by using method"""
    assert isinstance({}, dict)
    assert isinstance(set(), set)


def test_if_sets_are_hashable():
    """Frozenset is a hashable set. """
    x = {1, 2, 3}
    y = frozenset(x)
    assert not isinstance(x, Hashable)
    assert isinstance(y, Hashable)


def test_frozenset_creation():
    """Frozenset can be created only by using constructor frozenset()"""
    x = frozenset(range(10))
    assert isinstance(x, frozenset)
    assert x == frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})


def test_set_comprehension():
    """Set can be created by set comprehension."""
    some_list = [1, 1, 2, 3, 4, 2, 8, 'abc', True]
    some_set = {x for x in some_list if isinstance(x, int)}
    assert isinstance(some_set, set)
    assert some_set == {1, 2, 3, 4, 8}


def test_can_compare_set_and_frozenset():
    """Can compare set and frozenset with no issues"""
    x = {1, 2, 3}
    y = frozenset(x)
    z = {1, 2, 3, 4}
    assert x == y
    assert y == x
    assert y <= z


def test_add_set():
    """add() method adds an element to a set"""
    x = {1, 2, 3}
    x.add(4)
    assert x == {1, 2, 3, 4}


def test_add_frozenset():
    """add() method is not available for a frozenset"""
    x = frozenset({1, 2, 3})
    with pytest.raises(AttributeError, match="'frozenset' object has no attribute 'add'"):
        x.add(4)


def test_clear_set():
    """clear() removes all elements from a set"""
    x = {1, 2, 3}
    x.clear()
    assert x == set()


def test_clear_frozenset():
    """clear() method is not available for a frozenset"""
    x = frozenset({1, 2, 3})
    with pytest.raises(AttributeError, match="'frozenset' object has no attribute 'clear'"):
        x.clear()


def test_copy_set():
    """copy() returns a copy of a set"""
    x = {1, 2, 3}
    y = x.copy()
    assert x == y
    assert x is not y


def test_copy_frozenset():
    """copy() is available for a frozenset also"""
    x = frozenset(['a', 2, 3])
    y = x.copy()
    assert isinstance(y, frozenset)
    assert x == y
    assert x is y  # this looks a little odd for me
