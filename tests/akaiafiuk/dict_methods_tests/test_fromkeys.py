x = ('key1', 'key2', 'key3')
y = 0


def test_fromkeys_only_keys():
    """When create a dict from only one iterable, keys are None"""
    dictionary = dict.fromkeys(x)
    for key, value in dictionary.items():
        assert key in x
        assert value is None


def test_fromkeys_keys_one_value():
    """Can create a dict fromkeys with one default value from a variable"""
    dictionary = dict.fromkeys(x, y)
    for value in dictionary.values():
        assert value == 0
