import pytest


def test_values_len(car):
    """has the same len as dict"""
    values = car.values()
    assert len(values) == len(car)


def test_changing_dict_change_values(car):
    """When a dict is updated, the values() object reflect these changes"""
    values = car.values()
    assert len(values) == 3
    car.popitem()
    assert len(values) == 2


def test_cannot_change_values_directly(car):
    """Changing value using values() object is not possible"""
    updated_value = 'updated_value'
    with pytest.raises(TypeError):
        values = car.values()
        values[0] = updated_value
    assert updated_value not in car.values()


def test_cannot_subscribe_directly(car):
    """Cannot even subscribe to a value directly"""
    with pytest.raises(TypeError):
        values = car.values()
        print(values[0])
