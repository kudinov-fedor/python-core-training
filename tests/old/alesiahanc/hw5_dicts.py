import pytest

# DICTS
some_dict = {"a": 123, "b": 456, "c": 789}
some_dict_2 = {"c": 789, "a": 123, "b": 456}
some_dict_3 = dict.fromkeys("abc")
wierd_dict = {"a": 1, 2: "b",
              None: "abc",
              (1, "a"): "some",
              True: "kek",
              frozenset((1, 2)): "lol"}
data = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
        {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
        {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
        {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}]


def test_order_comparison():
    assert some_dict == some_dict_2


def test_get_element_dict():
    assert some_dict.get("a") == some_dict["a"]


@pytest.mark.parametrize(["value", "second_value", "expected"], [
    ("invalid", None, None),
    ("invalid", "default", "default")
])
def test_get_invalid_param(value, expected, second_value):
    result = some_dict.get(value, second_value)
    assert result == expected


def test_copy_dictionaries():
    copied_dict = some_dict.copy()
    assert copied_dict == some_dict
    assert copied_dict is not some_dict

# comprehension explanation
# newlist = [expression for item in iterable if bool(condition) == True]


@pytest.mark.parametrize(["arg", "expected"], [
    ("John", {'age': 16, 'second_name': 'Parris', 'name': 'John', 'sex': 'M'}),
    ("Marry", {'age': 15, 'second_name': 'Katon', 'name': 'Marry', 'sex': 'F'})
])
def test_search_by_name(arg, expected):
    by_name = {i["name"]: i for i in data}
    assert by_name[arg] == expected
