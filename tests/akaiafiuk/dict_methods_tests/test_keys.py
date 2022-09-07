import pytest


def test_keys_len(car):
    """has the same len as dict"""
    keys = car.keys()
    assert len(keys) == len(car)


def test_changing_dict_change_keys(car):
    """When a dict is updated, the keys() object reflect these changes"""
    keys = car.keys()
    assert len(keys) == 3
    car.popitem()
    assert len(keys) == 2


def test_cannot_change_keys_directly(car):
    """Changing key using keys() object is not possible"""
    updated_key = 'updated_key'
    with pytest.raises(TypeError):
        keys = car.keys()
        keys[0] = updated_key
    assert updated_key not in car


def test_side_effect_when_removing_dict_items(car):
    """
    Looping is not possible when changing dict during iteration
    But in the first iteration the dict do change
    """
    original_len = len(car)
    with pytest.raises(RuntimeError):
        for key in car.keys():
            car.pop(key)
    assert len(car) == original_len - 1


def test_convert_to_tuple_to_unlink_from_dict(car):
    """
    Looping is not possible when changing dict during iteration
    But in the first iteration the dict do change
    """
    for key in tuple(car.keys()):
        car.pop(key)
    assert len(car) == 0
