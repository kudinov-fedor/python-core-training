import pytest

CAR = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


def test_items_len():
    """has the same len as dict"""
    items = CAR.items()
    assert len(items) == len(CAR)


def test_items_tuples():
    """contains key-value pairs as tuples"""
    items = CAR.items()
    items_keys = [item[0] for item in items]
    items_values = [item[1] for item in items]
    assert list(CAR.keys()) == items_keys
    assert list(CAR.values()) == items_values


def test_changing_dict_value_change_items():
    """When an item in the dictionary changes value, the view object also gets updated"""
    items = CAR.items()
    assert list(items)[0][1] == 'Ford'
    CAR['brand'] = 'Audi'
    assert list(items)[0][1] == 'Audi'


def test_adding_items_to_dict_affects_items():
    """When an item is added to a dict, the items object also gets updated"""
    items = CAR.items()
    assert len(items) == 3
    CAR['driver'] = 'Anton'
    assert len(items) == 4


def test_cannot_change_items_directly():
    """This means that the items view cannot be changed"""
    items = CAR.items()
    with pytest.raises(TypeError):
        items[0] = 'test'


def test_convert_then_change():
    """This means that need to convert to other type to change"""
    items = list(CAR.items())
    items[0] = 'test'
    assert items[0] == 'test'
