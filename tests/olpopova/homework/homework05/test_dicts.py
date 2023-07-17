from olpopova.homework.homework05.dicts import filter_by_property


def test_filter_by_property():
    data = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
            {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
            {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
            {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}]
    assert filter_by_property(data) == (2, 2)
