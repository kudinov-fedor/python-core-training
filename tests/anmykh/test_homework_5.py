import pytest


@pytest.mark.parametrize(["param", "data_type"], [
    ({"a": 123, "b": 456, "c": 789}, dict),
    ({"a": 123, "b": 456, "c": 789}, dict),
    ({"c": 789, "a": 123, "b": 456}, dict),
    ({"a": 1, 2: "b",
      None: "abc",
      (1, "a"): "some",
      True: "kek",
      frozenset((1, 2)): "lol"}, dict)
])
def test_is_dict(param, data_type):
    assert isinstance(param, data_type)


@pytest.mark.parametrize(["dict_collection", "key", "result"], [
    ({"a": "1", "b": "2"}, "a", '1'),
    ({"c": "a", "a": "b"}, "c", 'a'),
    ({"m": None, "v": None}, "m", None)
])
def test_update_dict(dict_collection, key, result):
    assert dict_collection.get(key) == result


def test_error_func():
    with pytest.raises(ArithmeticError):
       5 / 0


def test_error_func_2():
    a = []
    with pytest.raises(IndexError):
        a[0]


def test_error_func_3():
    with pytest.raises(NameError):
        x


def test_error_func_24():
    a = []
    with pytest.raises(LookupError):
        a[0]
