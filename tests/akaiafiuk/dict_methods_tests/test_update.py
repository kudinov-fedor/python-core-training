import pytest

UPDATE_DICT = {3: 'three', 4: 'four', 5: 'five'}
UPDATE_LIST = [(3, 'three'), (4, 'four'), (5, 'five')]
UPDATE_ZIP = zip([3, 4, 5], ['three', 'four', 'five'])
BAD_TUPLE_LIST_THREE_ELEMENTS = [(3, 'three'), (4, 'four', 'five'), (5, 'five')]
BAD_TUPLE_LIST_UNHASHABLE = [(3, 'three'), ([4, ], 'four'), (5, 'five')]


def test_update_with_another_dict(default_dict):
    """Can update with another dict"""
    default_dict.update(UPDATE_DICT)
    assert default_dict == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


def test_update_list_tuples(default_dict):
    """Can update with list of tuples"""
    default_dict.update(UPDATE_LIST)
    assert default_dict == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


def test_update_zip(default_dict):
    """Can update with zip object"""
    default_dict.update(UPDATE_ZIP)
    assert default_dict == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


def test_update_with_three_elements_tuple():
    """
    Some kind of side effect
    when update with list of tuples and one of the tuples is bad (e.g too much values),
    update() will iterate through the list and add k: v pair
    but return ValueError when reach bad tuple
    """
    some_dict = dict()
    assert len(some_dict) == 0
    with pytest.raises(ValueError):
        some_dict.update(BAD_TUPLE_LIST_THREE_ELEMENTS)
    assert len(some_dict) == 1


def test_update_with_three_elements_tuple():
    """
    Some kind of side effect
    when update with list of tuples and one of the tuples is bad (e.g unhashable first element),
    update() will iterate through the list and add k: v pair
    but return ValueError when reach bad tuple
    """
    some_dict = dict()
    assert len(some_dict) == 0
    with pytest.raises(TypeError):
        some_dict.update(BAD_TUPLE_LIST_UNHASHABLE)
    assert len(some_dict) == 1
