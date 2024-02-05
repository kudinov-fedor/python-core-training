# DICTS
import pytest

some_dict = {"a": 123, "b": 456, "c": 789}
some_dict_2 = {"c": 789, "a": 123, "b": 456}
some_dict_3 = dict.fromkeys("abc")
wierd_dict = {"a": 1, 2: "b",
              None: "abc",
              (1, "a"): "some",
              True: "kek",
              frozenset((1, 2)): "lol"}


# is container
def test_dict_comparison():
    assert some_dict == some_dict_2
    assert "a" in some_dict
    assert len(some_dict) == 3
    assert list(some_dict_2) == ['c', 'a', 'b']


def test_dict_methods():
    assert some_dict["a"] == 123
    assert some_dict.get("a") == 123
    assert some_dict["a"] == some_dict.get("a")
    assert some_dict.get("invalid") == None
    assert some_dict.get("invalid", "default_val") == 'default_val'


@pytest.mark.parametrize("some", [{"a": 1, "b": 2}])
def test_dict_update(some):
    some.update({"b": "b", "c": "c"})
    assert some['a'] == 1
    assert some['b'] != 2
    assert some['b'] == 'b'
    assert some['c'] == 'c'


@pytest.mark.parametrize("some", [{"a": 1, "b": 2}])
def test_dict_copy(some):
    sopy_of_some = some.copy()
    assert sopy_of_some == some
    assert some['a'] == 1
    assert some['b'] == 2

    some.clear()
    assert some == {}


@pytest.mark.parametrize("some", [{"a": 1, "b": 2}])
def test_dict_methods(some):
    item = some.pop("a")
    assert item == 1
    assert 'a' not in some

    item = some.pop("invalid", "default_val")
    assert item == "default_val"

    item = some.setdefault("a", "default_for_a")
    assert "a" in some
    assert item == some['a']

    item = some.setdefault("a", "default_for_a")
    assert "a" in some
    assert some["a"] == "default_for_a"
    assert item == "default_for_a"

    item = some.setdefault("a", "other_default_for_a")
    assert "a" in some
    assert "a" in item
    assert some['a'] == "default_for_a"
    assert item == "default_for_a"


def test_dict_comprehension():
    some_dict = {"a": 123, "b": 456, "c": 789}

    dict1 = {k: v for k, v in some_dict.items()}
    assert dict1 == some_dict

    dict2 = {k * 2: str(v) for k, v in some_dict.items()}
    assert dict2 == {'aa': '123', 'bb': '456', 'cc': '789'}

    dict3 = {k: v for k, v in some_dict.items() if k <= "b"}
    assert dict3 == {'a': 123, 'b': 456}


def test_index_by_name():
    data = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
            {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
            {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
            {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}]
    by_name = {i["name"]: i for i in data}
    assert by_name["John"] == {'age': 16, 'second_name': 'Parris', 'name': 'John', 'sex': 'M'}
    assert by_name["Marry"] == {'age': 15, 'second_name': 'Katon', 'name': 'Marry', 'sex': 'F'}

    by_name = {(i["name"], i["second_name"]): i for i in data}
    assert by_name["John", "Parris"] == {'age': 16, 'second_name': 'Parris', 'name': 'John', 'sex': 'M'}
    assert by_name["Marry", "Katon"] == {'age': 15, 'second_name': 'Katon', 'name': 'Marry', 'sex': 'F'}

    by_sex = {}
    for i in data:
        if i["sex"] not in by_sex:
            by_sex[i["sex"]] = []
        by_sex[i["sex"]].append(i)
    assert len(by_sex["M"]) == 2
    assert len(by_sex["F"]) == 2

    by_sex = {}
    for i in data:
        by_sex.setdefault(i["sex"], []).append(i)
    assert len(by_sex["M"]) == 2
    assert len(by_sex["F"]) == 2


    from collections import defaultdict
    by_sex = defaultdict(list)
    for i in data:
        by_sex[i["sex"]].append(i)
    assert len(by_sex["M"]) == 2
    assert len(by_sex["F"]) == 2
