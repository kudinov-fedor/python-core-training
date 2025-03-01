import pytest

LAST_PAIR = ("year", 1964)
ADD_VALUE = [('driver', 'Anton')]


def test_popitem(car):
    """Basic scenario. Last added k: v pair is returned as a tuple and gets removed from dict"""
    original_len = len(car)
    popped = car.popitem()
    assert isinstance(popped, tuple)
    assert popped == LAST_PAIR
    assert len(car) == original_len - 1


def test_popitem_after_dict_update(car):
    """Add a k: v pair to a dict. This k: v pair is returned and gets removed by using popitem"""
    car.update(ADD_VALUE)
    popped = car.popitem()
    assert popped == ADD_VALUE[0]


def test_popitem_from_empty_dict():
    """Add a k: v pair to a dict. This k: v pair is returned and gets removed by using popitem"""
    empty_dict = dict()
    with pytest.raises(KeyError):
        empty_dict.popitem()
