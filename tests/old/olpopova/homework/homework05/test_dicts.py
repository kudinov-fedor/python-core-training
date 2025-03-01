from olpopova.homework.homework05.dicts import group_by


def test_group_by():
    data = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
            {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
            {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
            {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"},
            {"age": 78, "second_name": "Smith", "name": "John", "sex": "M"}
            ]
    expected = {"Marry": [{"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
                          {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"}],
                "John": [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
                         {"age": 78, "second_name": "Smith", "name": "John", "sex": "M"}],
                "Mathew": [{"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}]
                }
    assert group_by(data, 'name') == expected
