import pytest


@pytest.mark.parametrize(["arg1", "arg2", "expected"], [
    ("10110101", 2, 181),
    ("0b10110101", 2, 181),
    ("10110101", 2, 181)
])
def test_conversion_int(arg1, arg2, expected):
    assert expected == (int(arg1, arg2))


@pytest.mark.parametrize(["func", "arg", "expected"], [
    (int, "123", 123),
    (int, 123.0, 123),
    (float, "123", 123.0),
    (str, None, "None"),
    (list, "abc", ['a', 'b', 'c']),
    (list, {"a": 1, "b": 2}, ['a', 'b']),  # by default conversion by keys
    (list, (1, 2, 3), [1, 2, 3]),
    (tuple, "abc", ('a', 'b', 'c'))
])
def test_convert_without_parameters(func, arg, expected):
    assert expected == func(arg)


@pytest.mark.parametrize(["arg1", "arg2"], [
    ("abc", {'a', 'b', 'c'}),
    ({"a": 1, "b": 2}, {'a', 'b'}),
    ("aabcc", {'a', 'b', 'c'})  # no duplicates in sets
])
def test_conversion_sets(arg1, arg2):
    assert set() == set(arg1).difference(arg2)  # set can be returned in any order, so we need to check that all elements are there


@pytest.mark.parametrize(["arg", "expected"], [
    ([("a", 123), ("b", 456)], {'a': 123, 'b': 456}),
    ({"a": 1, "b": 2}, {'a': 1, 'b': 2})
])
def test_conversion_dictionaries(arg, expected):
    assert expected == dict(arg)


@pytest.mark.parametrize(["arg1", "arg2", "func", "expected"], [
    (["a", "b", "c"], [1, 2, 3], zip, {'a': 1, 'b': 2, 'c': 3})
])
def test_conversion_dict_functions(arg1, arg2, func, expected):
    assert expected == dict(func(arg1, arg2))
