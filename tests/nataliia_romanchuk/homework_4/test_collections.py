import pytest

some_str = "abcd"
some_tuple = "a", "b", "c", "d"
some_list = ["a", "b", "c", "d"]
some_set = {"a", "b", "c", "d"}
some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}


# len
def test_len_string():
    assert len(some_str) == 4


def test_len_tuple():
    assert len(some_tuple) == 4


def test_len_list():
    assert len(some_list) == 4


def test_len_set():
    assert len(some_set) == 4


def test_len_dict():
    assert len(some_dict) == 4


# contains
def test_in_string():
    assert "a" in some_str


def test_in_tuple():
    assert "a" in some_tuple


def test_in_list():
    assert "a" in some_list


def test_in_set():
    assert "a" in some_set


def test_in_dict_keys():
    assert "a" in some_dict


def test_in_dict_values():
    assert "a" in some_dict.keys()
    assert "a" not in some_dict.values()


# getitem
def test_indexing_string():
    assert some_str[0] == "a"


def test_indexing_tuple():
    assert some_tuple[0] == "a"


def test_indexing_list():
    assert some_list[0] == "a"


def test_indexing_dict():
    assert some_dict["a"] == 123


# last item
def test_last_item_string():
    assert some_str[-1] == "d"


def test_last_item_tuple():
    assert some_tuple[-1] == "d"


def test_last_item_list():
    assert some_list[-1] == "d"


# modify
def test_modify_and_delete_list():
    a = [1, 2, 3, 4]
    a[3] = "abc"
    assert a[3] == "abc"


def test_delete_from_list():
    a = [1, 2, 3, 4]
    del a[1]
    assert a == [1, 3, 4]


def test_modify_dict():
    b = {"a": 123, "b": 456}
    b["c"] = 7889
    assert b["c"] == 7889


def test_modify_dict():
    b = {"a": 123, "b": 456}
    b["b"] = "some"
    assert b["b"] == "some"


def test_delete_from_dict():
    b = {"a": 123, "b": 456}
    del b["a"]
    assert "a" not in b


# unpack / iterate
def test_list_conversion():
    assert list(some_str) == ['a', 'b', 'c', 'd']
    assert list(some_tuple) == ['a', 'b', 'c', 'd']
    assert list(some_list) == ['a', 'b', 'c', 'd']
    assert sorted(some_set) == ['a', 'b', 'c', 'd']
    assert list(some_dict) == ['a', 'b', 'c', 'd']


def test_tuple_conversion():
    assert tuple(some_str) == ('a', 'b', 'c', 'd')
    assert tuple(some_tuple) == ('a', 'b', 'c', 'd')
    assert tuple(some_list) == ('a', 'b', 'c', 'd')
    assert tuple(sorted(some_set)) == ('a', 'b', 'c', 'd')
    assert tuple(sorted(some_dict)) == ('a', 'b', 'c', 'd')


# multiple assignment
def test_multiple_assignment():
    a, b, c, d = some_tuple
    assert (a, b, c, d) == ('a', 'b', 'c', 'd')

    a, b, c, d = some_list
    assert (a, b, c, d) == ('a', 'b', 'c', 'd')

    sorted_set = sorted(some_set)
    assert sorted_set == ['a', 'b', 'c', 'd']

    a, b, c, d = sorted(some_dict)
    assert (a, b, c, d) == ('a', 'b', 'c', 'd')

    sorted_set = sorted(some_set)
    a, b, c, d = sorted_set
    assert (a, b, c, d) == ('a', 'b', 'c', 'd')


@pytest.mark.parametrize("input_data, expected", [
    (some_str, ('a', ['b', 'c', 'd'])),
    (some_tuple, ('a', ['b', 'c', 'd'])),
    (some_list, ('a', ['b', 'c', 'd'])),
])
def test_unpacking(input_data, expected):
    a, *tail = input_data
    assert (a, tail) == expected


def test_unpacking_sets():
    a, *tail = sorted(some_set)
    assert a == 'a'
    assert set(tail) == {'b', 'c', 'd'}


def test_unpacking_dicts():
    a, *tail = sorted(some_dict)
    assert a == 'a'
    assert set(tail) == {'b', 'c', 'd'}


def test_unpacking_strings_head():
    *head, d = some_str
    assert (head, d) == (['a', 'b', 'c'], 'd')


def test_unpacking_tuples_head():
    *head, d = some_tuple
    assert (head, d) == (['a', 'b', 'c'], 'd')


def test_unpacking_lists_head():
    *head, d = some_list
    assert (head, d) == (['a', 'b', 'c'], 'd')


def test_unpacking_sets_head_d():
    *head, d = sorted(some_set)
    assert set(head) == {'a', 'b', 'c'}
    assert d == 'd'


def test_unpacking_dicts_head():
    *head, d = some_dict
    assert set(head) == {'a', 'b', 'c'}
    assert d == 'd'


def test_unpacking_strings_a_middle_d():
    a, *middle, d = some_str
    assert (a, middle, d) == ('a', ['b', 'c'], 'd')


def test_unpacking_tuples_a_middle_d():
    a, *middle, d = some_tuple
    assert (a, middle, d) == ('a', ['b', 'c'], 'd')


def test_unpacking_lists_a_middle_d():
    a, *middle, d = some_list
    assert (a, middle, d) == ('a', ['b', 'c'], 'd')


def test_unpacking_sets_a_middle_d():
    a, *middle, d = sorted(some_set)
    assert a == 'a'
    assert middle == ['b', 'c']
    assert d == 'd'


def test_unpacking_dicts_a_middle_d():
    a, *middle, d = sorted(some_dict)
    assert a == 'a'
    assert middle == ['b', 'c']
    assert d == 'd'


def test_unpacking_strings():
    a, b, c, d, *tail = some_str
    assert (a, b, c, d, tail) == ('a', 'b', 'c', 'd', [])


def test_unpacking_tuples():
    a, b, c, d, *tail = some_tuple
    assert (a, b, c, d, tail) == ('a', 'b', 'c', 'd', [])


def test_unpacking_lists():
    a, b, c, d, *tail = some_list
    assert (a, b, c, d, tail) == ('a', 'b', 'c', 'd', [])


def test_unpacking_sets():
    a, b, c, d, *tail = sorted(some_set)
    assert a == 'a'
    assert b == 'b'
    assert c == 'c'
    assert d == 'd'
    assert tail == []


def test_unpacking_dicts():
    a, b, c, d, *tail = sorted(some_dict)
    assert a == 'a'
    assert b == 'b'
    assert c == 'c'
    assert d == 'd'
    assert tail == []


# iterate protocol
def test_iterator_for_string():
    some_str_iter = iter(some_str)
    first_item = next(some_str_iter)
    assert first_item == 'a'

    rest_items = list(some_str_iter)
    assert rest_items == ['b', 'c', 'd']

    exhausted_items = list(some_str_iter)
    assert exhausted_items == []


@pytest.mark.parametrize("expected_first, expected_rest, expected_exhausted", [
    ('a', ['b', 'c', 'd'], [])])
def test_iterator_for_tuple(expected_first, expected_rest, expected_exhausted):
    some_tuple_iter = iter(some_tuple)

    first_item = next(some_tuple_iter)
    assert first_item == expected_first

    rest_items = list(some_tuple_iter)
    assert rest_items == expected_rest

    exhausted_items = list(some_tuple_iter)
    assert exhausted_items == expected_exhausted


@pytest.mark.parametrize("expected_first, expected_rest, expected_exhausted", [
    ('a', ['b', 'c', 'd'], [])])
def test_iterator_for_list(expected_first, expected_rest, expected_exhausted):
    some_list_iter = iter(some_list)

    first_item = next(some_list_iter)
    assert first_item == expected_first

    rest_items = list(some_list_iter)
    assert rest_items == expected_rest

    exhausted_items = list(some_list_iter)
    assert exhausted_items == expected_exhausted


def test_iterator_for_set():
    sort = sorted(some_set)
    some_set_iter = iter(sort)

    first_item = next(some_set_iter)
    assert first_item in ['a', 'b', 'c', 'd']

    rest_items = list(some_set_iter)
    assert rest_items == ['b', 'c', 'd']

    exhausted_items = list(some_set_iter)
    assert exhausted_items == []


def test_iterator_for_dict():
    some_dict_iter = iter(sorted(some_dict))

    first_key = next(some_dict_iter)
    assert first_key in ['a', 'b', 'c', 'd']

    rest_keys = list(some_dict_iter)
    assert rest_keys == ['b', 'c', 'd']

    exhausted_keys = list(some_dict_iter)
    assert exhausted_keys == []


# sort data (same for min max)
data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]


def test_sort_data_by_age():
    sorted_data_ascending = sorted(data, key=lambda i: i["age"])
    sorted_data_descending = sorted(data, key=lambda i: i["age"], reverse=True)
    assert [i["age"] for i in sorted_data_ascending] == [16, 25, 34]
    assert [i["age"] for i in sorted_data_descending] == [34, 25, 16]


def test_sort_data_by_sex_and_age_and_name():
    # sort by sex (F first) and age (asc)sorted(data, key=lambda i: (i["sex"] == "M", i["age"]))
    sorted_data_sex_age_asc = sorted(data, key=lambda i: (i["sex"] == "M", i["age"]))
    assert [i['sex'] for i in sorted_data_sex_age_asc] == ['F', 'M', 'M']
    assert [i['age'] for i in sorted_data_sex_age_asc] == [34, 16, 25]

    # sort by sex (F first) and age (desc)
    sorted_data_sex_age_desc = sorted(data, key=lambda i: (i["sex"] == "M", -i["age"]))
    assert [i['sex'] for i in sorted_data_sex_age_asc] == ['F', 'M', 'M']
    assert [i['age'] for i in sorted_data_sex_age_asc] == [34, 16, 25]

    # sort by name  alphabetically
    sorted_data_by_name = sorted(data, key=lambda i: i["name"])
    assert [i['name'] for i in sorted_data_by_name] == ["John", "Marry", "Mathew"]


# # zip, enumerate, reversed, map, filter
def test_filter():
    filtered_data = list(filter(lambda i: i["sex"] == "M", data))
    assert filtered_data == [{"age": 16, "name": "John", "sex": "M"},
                             {"age": 25, "name": "Mathew", "sex": "M"}]


def test_enumerate():
    data_enum = list(enumerate(data))
    assert enumerated_data == [(0, {"age": 16, "name": "John", "sex": "M"}),
                               (1, {"age": 34, "name": "Marry", "sex": "F"}),
                               (2, {"age": 25, "name": "Mathew", "sex": "M"})]


def test_revers():
    reversed_data = list(reversed(data))
    assert reversed_data == [{"age": 25, "name": "Mathew", "sex": "M"},
                             {"age": 34, "name": "Marry", "sex": "F"},
                             {"age": 16, "name": "John", "sex": "M"}]


def test_map():
    mapped_data = list(map(lambda i: i["name"], data))
    assert mapped_data == ["John", "Marry", "Mathew"]


def test_zip():
    zipped_data_1 = list(zip(data, [1, 2, 3, 4, 5, 6, 7]))
    assert zipped_data_1 == [
        ({"age": 16, "name": "John", "sex": "M"}, 1),
        ({"age": 34, "name": "Marry", "sex": "F"}, 2),
        ({"age": 25, "name": "Mathew", "sex": "M"}, 3)
    ]


def test_zip12():
    zipped_data_2 = list(zip(data, [1, 2]))
    assert zipped_data_2 == [
        ({"age": 16, "name": "John", "sex": "M"}, 1),
        ({"age": 34, "name": "Marry", "sex": "F"}, 2)
    ]


def test_zip123():
    zipped_data_3 = list(zip(data, [1, 2, 3]))
    assert zipped_data_3 == [
        ({"age": 16, "name": "John", "sex": "M"}, 1),
        ({"age": 34, "name": "Marry", "sex": "F"}, 2),
        ({"age": 25, "name": "Mathew", "sex": "M"}, 3)
    ]
