def test_new_my_list():
    some_list = [1, 2, 3, 4, 5]
    result = [i for i in some_list]
    assert some_list == result


def test_comprehension_with_filtration():
    some_list2 = [1, 2, 3, 5, 10, 12]
    filtering_result = [i * 2 for i in some_list2 if i <= 3]
    expected = [2, 4, 6]
    assert filtering_result == expected


def test_dict_comprehension():
    some_dict = {"a": 1, "b": 2, "c": 3}
    processing_dict_in_comprehensions_resut = [some_dict[k] * 2 for k in some_dict if some_dict[k] <= 2]
    expected = [2, 4]
    assert processing_dict_in_comprehensions_resut == expected


def test_collect_data():
    """
    the sorted list of ages is converted back to a set using set(ages)
    """
    data = [{"age": 16, "name": "John", "sex": "M"},
            {"age": 34, "name": "Marry", "sex": "F"},
            {"age": 25, "name": "Mathew", "sex": "M"}]

    ages = sorted({i["age"] for i in data}, reverse=True)
    expected = {34, 25, 16}
    assert set(ages) == expected

