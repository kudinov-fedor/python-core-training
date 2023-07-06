import pytest

some_dict = {"a": 123, "b": 456, "c": 789}
some_dict_2 = {"c": 789, "a": 123, "b": 456}
some_dict_3 = dict.fromkeys("abc")
wierd_dict = {"a": 1, 2: "b",
              None: "abc",
              (1, "a"): "some",
              True: "kek",
              frozenset((1, 2)): "lol"}


def test_dict_compar():
    assert some_dict == some_dict_2


def test_update_method():
    some = {"a": 1, "b": 2}
    some.update({"b": "b", "c": "c"})
    assert some == {"a": 1, "b": "b", "c": "c"}


def test_copy_method():
    some = {"a": 1, "b": 2}
    copy_of_some = some.copy()
    assert some == copy_of_some


def test_setdefault():
    some = {"a": 1, "b": 2}
    item = some.setdefault("a", "default_for_a")
    assert item == 1
    assert some["a"] is not "default_for_a"


def test_dict_comprehension():
    some_new_dict = {k * 2: str(v) for k, v in some_dict.items()}
    expected_res = {"aa": "123", "bb": "456", "cc": "789"}
    assert some_new_dict == expected_res


def test_dict_comprehension_2():
    some_new_dict = {k: v for k, v in some_dict.items() if k <= "b"}
    expected_res = {"a": 123, "b": 456}
    assert some_new_dict == expected_res


data = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
        {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
        {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
        {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}]


def test_dict_index():
    by_name = {i["name"]: i for i in data}
    expected_dict = {"John": {"age": 16, "name": "John", "second_name": "Parris", "sex": "M"},
                     "Marry": {"age": 15, "name": "Marry", "second_name": "Katon", "sex": "F"},
                     "Mathew": {"age": 25, "name": "Mathew", "second_name": "Maton", "sex": "M"}}
    assert by_name == expected_dict


def test_dict_index_2():
    by_name = {(i["name"], i["second_name"]): i for i in data}
    expected_dict = {('John', 'Parris'): {'age': 16, 'second_name': 'Parris', 'name': 'John', 'sex': 'M'},
                     ('Marry', 'Atkinson'): {'age': 34, 'second_name': 'Atkinson', 'name': 'Marry', 'sex': 'F'},
                     ('Marry', 'Katon'): {'age': 15, 'second_name': 'Katon', 'name': 'Marry', 'sex': 'F'},
                     ('Mathew', 'Maton'): {'age': 25, 'second_name': 'Maton', 'name': 'Mathew', 'sex': 'M'}}
    assert by_name == expected_dict


def test_dict_index_by_sex():
    by_name = {i["sex"]: i for i in data}
    expected_dict = {"M": {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"},
                     "F": {'age': 15, 'second_name': 'Katon', 'name': 'Marry', 'sex': 'F'}}
    assert by_name == expected_dict


data_1 = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
          {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
          {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
          {"age": 25, "second_name": "Maton", "name": "John", "sex": "M"}]


def test_group_by():
    by_name = {}
    for i in data_1:
        if i["name"] not in by_name:
            by_name[i["name"]] = []
        by_name[i["name"]].append(i)
    expected_dict = {"John": [{"age": 16, "name": "John", "second_name": "Parris", "sex": "M"},
                              {"age": 25, "name": "John", "second_name": "Maton", "sex": "M"}],
                     "Marry": [{"age": 34, "name": "Marry", "second_name": "Atkinson", "sex": "F"},
                               {"age": 15, "name": "Marry", "second_name": "Katon", "sex": "F"}]}
    assert by_name == expected_dict
    assert len(by_name["John"]) == 2
    assert len(by_name["Marry"]) == 2
