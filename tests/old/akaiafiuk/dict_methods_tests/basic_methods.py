a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('two', 2), ('three', 3)])
e = dict({'one': 1, 'two': 2, 'three': 3})


def test_all_dicts_are_eql():
    """Different ways of creating a dictionary"""
    assert a == b == c == d == e


def test_clear(default_dict):
    """clear() method removes all the elements from a dict"""
    default_dict.clear()
    assert default_dict == {}
