import pytest

some_list = [1, 2, 3, 4, 5]
some_dict = {"a": 1, "b": 2, "c": 3}


def test_check_dict_comprehension():
    assert {i: i * 2 for i in some_list} == {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}


def test_check_filtered_compr():
    assert [i * 2 for i in some_list if i <= 3] == [2, 4, 6]


def test_check_filtered_compr_2():
    assert {i: i * 2 for i in some_list if i <= 3} == {1: 2, 2: 4, 3: 6}


def test_process_dict():
    assert [some_dict[k] * 2 for k in some_dict if some_dict[k] <= 2] == [2, 4]


def test_process_dict_2():
    assert {i[0]: i[1] for i in some_dict.items()} == {"a": 1, "b": 2, "c": 3}


def test_process_dict_3():
    assert {k * 2: v * 2 for k, v in some_dict.items() if v <= 2} == {"aa": 2, "bb": 4}


data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]


def test_collect_data():
    ages = {i["age"] for i in data}
    names = {i["name"] for i in data}
    assert ages == {16, 34, 25}
    assert names == {"John", "Marry", "Mathew"}
