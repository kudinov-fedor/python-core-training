import pytest

some_str = "abcd"
some_tuple = "a", "b", "c", "d"
some_list = ["a", "b", "c", "d"]
some_set = {"a", "b", "c", "d"}
some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}
data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]


@pytest.mark.parametrize("param", [
    some_str,
    some_tuple,
    some_list,
    some_set,
    some_dict
])
def test_check_contains(param):
    assert "a" in param


@pytest.mark.parametrize(["par1", "res"], [
    (some_str[0], "a"),  # by index
    (some_tuple[0], "a"),  # by index
    (some_list[0], "a"),  # by index
    (some_dict["a"], 123),
    (some_str[-1], "d"),
    (some_tuple[-1], "d"),
    (some_list[-1], "d")
])
def test_check_index_last(par1, res):
    assert par1 == res, f"Result = {res}"


def test_check_lis_modifications():
    a = [1, 2, 3, 4]
    a[3] = "abc"
    del a[1]
    result = [1, 3, "abc"]
    assert a == result, f"Result = {a}"


def test_check_collection_modif():
    b = {"a": 123, "b": 456}
    b["c"] = 7889
    b["b"] = "some"
    del b["a"]
    results = {"b": "some", "c": 7889}
    assert b == results, f"Result is {b}"


def test_check_unpack():
    some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}
    some_new_list = sorted(list(some_dict))
    list_result = ["a", "b", "c", "d"]
    assert some_new_list == list_result, f"New list: {some_new_list}"


def test_check_tuple_unpacking():
    some_tuple = "a", "b", "c", "d"
    *head, d = some_tuple
    assert head == ["a", "b", "c"]
    assert d == "d"


def test_check_dic_unpack():
    some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}
    a, *middle, d = sorted(some_dict)
    assert a == "a"
    assert middle == ["b", "c"]
    assert d == "d"


def test_check_str_itter():
    some_str_iter = iter(some_str)
    assert next(some_str_iter) == "a"
    assert list(some_str_iter) == ["b", "c", "d"]
    assert list(some_str_iter) == []


def test_check_tuple_itter():
    some_tuple_iter = iter(some_tuple)
    assert next(some_tuple_iter) == "a"
    assert list(some_tuple_iter) == ["b", "c", "d"]
    assert list(some_tuple_iter) == []


def test_check_set_itter():
    some_dict_iter = iter(some_dict)
    assert next(some_dict_iter) == "a"
    assert list(some_dict_iter) == ["b", "c", "d"]
    assert list(some_dict_iter) == []


def test_sort_by_age():
    sorted_data = sorted(data, key=lambda i: i["age"])
    result = [{"age": 16, "name": "John", "sex": "M"},
              {"age": 25, "name": "Mathew", "sex": "M"},
              {"age": 34, "name": "Marry", "sex": "F"}]
    assert sorted_data == result


def test_sort_by_sex():
    sorted_data = sorted(data, key=lambda i: i["sex"] == "M", reverse=True)
    result = [{"age": 16, "name": "John", "sex": "M"},
              {"age": 25, "name": "Mathew", "sex": "M"},
              {"age": 34, "name": "Marry", "sex": "F"}]
    assert sorted_data == result


def test_data_enumerate():
    assert list(enumerate(data)) == [
        (0, {"age": 16, "name": "John", "sex": "M"}),
        (1, {"age": 34, "name": "Marry", "sex": "F"}),
        (2, {"age": 25, "name": "Mathew", "sex": "M"})
    ]


def test_map_data():
    assert list(map(lambda i: i["name"], data)) == ["John", "Marry", "Mathew"]


def test_zip_data():
    assert list(zip(data, [1, 2])) == [
        ({"age": 16, "name": "John", "sex": "M"}, 1),
        ({"age": 34, "name": "Marry", "sex": "F"}, 2)
    ]
