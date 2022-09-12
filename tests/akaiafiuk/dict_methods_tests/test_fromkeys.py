x = ('key1', 'key2', 'key3')
y = 0


def test_fromkeys_only_keys():
    """When create a dict from only one iterable, keys are None"""
    dictionary = dict.fromkeys(x)
    assert set(x).issubset(dictionary)
    for value in dictionary.values():
        assert value is None


def test_fromkeys_keys_one_value():
    """Can create a dict fromkeys with one default value from a variable"""
    dictionary = dict.fromkeys(x, y)
    assert set(dictionary.values()) == {0}
