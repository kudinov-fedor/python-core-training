import pytest

x = {1, 2, 3, 4, 'a'}
y = {3, 4, 5}
z = ['a', 'b', 'c', 1, 2, 3, 4, 4]


def test_intersection_operator():
    """Intersect two sets using operator. Can only intersect two elements at once."""
    answer = x & y
    assert answer == {3, 4}


def test_intersection_operator_negative():
    """Negative test. Error is displayed when intersecting with incorrect type"""
    with pytest.raises(TypeError):
        x & [3, 4, 5]


def test_intersection_method():
    """Intersect multiple sets using method. Can intersect multiple iterables"""
    answer = x.intersection(y, z)
    assert answer == {3, 4}


def test_intersection_update_operator():
    """&= will replace original set with intersection"""
    fruits = {'orange', 'apple', 'banana'}
    yellow_objects = {'banana', 'apple', 'chicken'}
    fruits &= yellow_objects
    assert fruits == {'banana', 'apple'}


def test_intersection_update_operator_negative():
    """&= can only work with same type"""
    fruits = {'orange', 'apple', 'banana'}
    yellow_objects = ['banana', 'apple', 'chicken']
    with pytest.raises(TypeError):
        fruits &= yellow_objects
    assert fruits == {'orange', 'apple', 'banana'}


def test_intersection_update_method():
    """using intersection_update() method can update set with multiple iterables at once"""
    fruits = {'orange', 'apple', 'banana'}
    yellow_objects = {'banana', 'apple', 'chicken'}
    fruits_list = ['orange', 'apple', 'banana']
    fruits.intersection_update(yellow_objects, fruits_list)
    assert fruits == {'banana', 'apple'}
