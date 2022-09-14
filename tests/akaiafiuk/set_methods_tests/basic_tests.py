from collections import Hashable


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
