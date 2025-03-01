import pytest


def test_items_len(car):
    """has the same len as dict"""
    items = car.items()
    assert len(items) == len(car)


def test_items_tuples(car):
    """contains key-value pairs as tuples"""
    items = car.items()
    items_keys = [item[0] for item in items]
    items_values = [item[1] for item in items]
    assert list(car.keys()) == items_keys
    assert list(car.values()) == items_values


def test_changing_dict_value_change_items(car):
    """When an item in the dictionary changes value, the view object also gets updated"""
    items = car.items()
    assert list(items)[0][1] == 'Ford'
    car['brand'] = 'Audi'
    assert list(items)[0][1] == 'Audi'


def test_adding_items_to_dict_affects_items(car):
    """When an item is added to a dict, the items object also gets updated"""
    items = car.items()
    assert len(items) == 3
    car['driver'] = 'Anton'
    assert len(items) == 4


def test_cannot_change_items_directly(car):
    """This means that the items view cannot be changed"""
    items = car.items()
    with pytest.raises(TypeError):
        items[0] = 'test'


def test_convert_then_change(car):
    """This means that need to convert to other type to change"""
    items = list(car.items())
    items[0] = 'test'
    assert items[0] == 'test'
