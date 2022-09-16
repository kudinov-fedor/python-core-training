import pytest

some_dict = {"A": 1, "B": 2, "C": 3}
some_big_set = set('A B D E F G H I J'.split())
some_set = {'A', 'B'}
some_other_set = {'B', 'C'}


def test_basic_issubset():
    """issubset() method checks if one set is subset of another set"""
    assert some_set.issubset(some_big_set)
    assert not some_other_set.issubset(some_big_set)


def test_issubset_check__keys_in_dict():
    """issubset() can check whether all required keys are in dict"""
    assert some_set.issubset(some_dict)


def test_issubset_operator_basic():
    """can use operator <= instead of issubset()"""
    assert some_set <= some_big_set
    assert not some_other_set <= some_big_set


def test_issubset_operator_negative():
    """operator <= can only work with the same type"""
    with pytest.raises(TypeError):
        some_set <= some_dict
