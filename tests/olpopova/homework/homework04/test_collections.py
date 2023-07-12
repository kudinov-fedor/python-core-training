import pytest

from olpopova.homework.homework04 import collections


data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]


@pytest.mark.parametrize(['data', 'sort_params', 'reverse', 'expected'], [
    (data, lambda i: i["age"], False, [{"age": 16, "name": "John", "sex": "M"},
                                       {"age": 25, "name": "Mathew", "sex": "M"},
                                       {"age": 34, "name": "Marry", "sex": "F"}]),
    (data, lambda i: i["age"], True, [{"age": 34, "name": "Marry", "sex": "F"},
                                      {"age": 25, "name": "Mathew", "sex": "M"},
                                      {"age": 16, "name": "John", "sex": "M"}]),
    (data, lambda i: i["sex"] == "M", False, [{"age": 34, "name": "Marry", "sex": "F"},
                                              {"age": 16, "name": "John", "sex": "M"},
                                              {"age": 25, "name": "Mathew", "sex": "M"}]),
    (data, lambda i: i["sex"] == "M", True, [{"age": 16, "name": "John", "sex": "M"},
                                             {"age": 25, "name": "Mathew", "sex": "M"},
                                             {"age": 34, "name": "Marry", "sex": "F"}]),
    (data, lambda i: (i["sex"] == "M", i["age"]), False, [{"age": 34, "name": "Marry", "sex": "F"},
                                                          {"age": 16, "name": "John", "sex": "M"},
                                                          {"age": 25, "name": "Mathew", "sex": "M"}]),
    (data, lambda i: (i["sex"] == "M", -i["age"]), False, [{"age": 34, "name": "Marry", "sex": "F"},
                                                           {"age": 25, "name": "Mathew", "sex": "M"},
                                                           {"age": 16, "name": "John", "sex": "M"}]),
    (data, lambda i: i["name"], False, [{"age": 16, "name": "John", "sex": "M"},
                                        {"age": 34, "name": "Marry", "sex": "F"},
                                        {"age": 25, "name": "Mathew", "sex": "M"}])
])
def test_sort(data, sort_params, reverse, expected):
    assert collections.sort(data, sort_params, reverse) == expected


@pytest.mark.parametrize(['data', 'filter_name', 'expected'], [
    (data, "name", ["John", "Marry", "Mathew"]),
    (data, "age", [16, 25, 34])
])
def test_filter(data, filter_name, expected):
    assert collections.filter_data(data, filter_name) == expected


@pytest.mark.parametrize(['collection', 'expected'], [
    ({'key1': 'param', 'key2': 123, 'key3': None}, ['key1', 'key2', 'key3']),
    ({(123, 456): 'kjdgg', (123, 654): 'kjdjd', ('jdjf', 'rrrr'): 1235}, [(123, 456), (123, 654), ('jdjf', 'rrrr')])
])
def test_unpack_dict(collection, expected):
    assert list(collection) == expected


@pytest.mark.parametrize(['collection', 'expected'], [
    ({'key1': 'param', 'key2': 123, 'key3': None}, ('key1', 'key2', 'key3')),
    ({(123, 456): 'kjdgg', (123, 654): 'kjdjd', ('jdjf', 'rrrr'): 1235}, ((123, 456), (123, 654), ('jdjf', 'rrrr')))
])
def test_unpack_dict(collection, expected):
    assert tuple(collection) == expected


def test_mult_assignment(collection="flgo"):
    assert collections.multiple_assignment(collection) == "First will be f, then - l, then - g and in the end - o"


def test_mult_assignment_tail(collection="flgo"):
    assert collections.mult_assignment_tail(collection) == ('f', ['l', 'g', 'o'])


def test_mult_assignment_head(collection="flgo"):
    assert collections.mult_assignment_head(collection) == (['f', 'l', 'g'], 'o')
