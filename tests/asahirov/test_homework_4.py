import pytest


def test_collections_sort():
    # sort data (same for min max)
    data = [{"age": 16, "name": "John", "sex": "M"},
            {"age": 34, "name": "Marry", "sex": "F"},
            {"age": 25, "name": "Mathew", "sex": "M"}]

    sorted_list = sorted(data, key=lambda i: i["age"])
    assert [i["age"] for i in sorted_list] == [16, 25, 34]

    sorted_list_reverse = sorted(data, key=lambda i: i["age"], reverse=True)
    assert [i["age"] for i in sorted_list_reverse] == [34, 25, 16]


def test_collections_sort_multiple():
    data = [{"age": 16, "name": "John", "sex": "M"},
            {"age": 34, "name": "Marry", "sex": "F"},
            {"age": 25, "name": "Mathew", "sex": "M"}]

    sorted_list = sorted(data, key=lambda i: (i["sex"] == "M", i["age"]))
    assert sorted_list[0]["name"] == "Marry"
    assert sorted_list[-1]["name"] == "Mathew"


def test_comprehensions_dict():
    some_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

    filtered_dict_keys = [i[0] for i in some_dict.items() if i[1] % 2 != 0]
    assert sorted(list("cea")) == sorted(filtered_dict_keys)


@pytest.mark.parametrize("password", ["some base password",
                                      "file base test",
                                      "text some test",
                                      "user text file",
                                      "softserve courses"])
def test_string_methods(password):
    rule = {"o": "0",
            "l": "1",
            "b": "8",
            "s": "5"}
    trans_table = str.maketrans(rule)
    updated_password = password.translate(trans_table)
    for orig_char, upd_char in zip(password, updated_password):
        if orig_char in rule:
            assert upd_char == rule[orig_char]
