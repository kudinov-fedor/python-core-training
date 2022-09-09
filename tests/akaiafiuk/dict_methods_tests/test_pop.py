import pytest

DEFAULT_VALUE = 'dummy_data'
EXISTING_KEY = 'brand'
EXISTING_VAL = 'Ford'
NON_EXISTENT_KEY = 'driver'


def test_pop_existing_key(car):
    """Popping is made by key, returns it's value and removes key: value pair from the dict"""
    original_len = len(car)
    assert EXISTING_KEY in car.keys()
    popped = car.pop(EXISTING_KEY)
    assert len(car) == original_len - 1
    assert EXISTING_KEY not in car.keys()
    assert popped == EXISTING_VAL


def test_pop_non_existent_key(car):
    """KeyError is raised when popping by non-existent key"""
    with pytest.raises(KeyError):
        car.pop(NON_EXISTENT_KEY)


def test_pop_non_existent_key_with_default(car):
    """
    However, can set default value as a second param and it will be returned
    and this value will be returned if the key is absent
    """
    pop_default = car.pop(NON_EXISTENT_KEY, DEFAULT_VALUE)
    assert pop_default == DEFAULT_VALUE


def test_pop_existing_key_with_default(car):
    """
    Pop existing key with default as a second param. Real value is returned.
    """
    pop_existing = car.pop(EXISTING_KEY, DEFAULT_VALUE)
    assert pop_existing == EXISTING_VAL


def test_pop_no_params(car):
    """TypeError is raised in case when called with no params"""
    with pytest.raises(TypeError):
        car.pop()


def test_pop_from_empty():
    """Error is raised in case when the key is absent"""
    empty_dict = dict()
    with pytest.raises(KeyError):
        empty_dict.pop(NON_EXISTENT_KEY)


def test_pop_from_empty_with_default():
    """No error when there is a default value"""
    empty_dict = dict()
    pop_default = empty_dict.pop(NON_EXISTENT_KEY, DEFAULT_VALUE)
    assert pop_default == DEFAULT_VALUE
