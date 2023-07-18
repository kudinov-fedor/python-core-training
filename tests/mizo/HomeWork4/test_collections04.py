import pytest

data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]


@pytest.mark.parametrize("data, sorting_by, reverse, expected", [
    (data, lambda i: i["age"], False, [{'age': 16, 'name': 'John', 'sex': 'M'},
                                       {'age': 25, 'name': 'Mathew', 'sex': 'M'},
                                       {'age': 34, 'name': 'Marry', 'sex': 'F'}]),
    (data, lambda i: i["age"], True, [{"age": 34, "name": "Marry", "sex": "F"},
                                      {"age": 25, "name": "Mathew", "sex": "M"},
                                      {"age": 16, "name": "John", "sex": "M"}]),
    (data, lambda i: i["name"], False, [{"age": 16, "name": "John", "sex": "M"},
                                        {"age": 34, "name": "Marry", "sex": "F"},
                                        {"age": 25, "name": "Mathew", "sex": "M"}]),
    (data, lambda i: i["name"], True, [{"age": 25, "name": "Mathew", "sex": "M"},
                                       {"age": 34, "name": "Marry", "sex": "F"},
                                       {"age": 16, "name": "John", "sex": "M"}])

])
def test_sorting(data, sorting_by, reverse, expected):
    result = sorted(data, key=sorting_by, reverse=reverse)
    assert result == expected


@pytest.mark.parametrize("data, expected", [
    (data, ['John', 'Marry', 'Mathew']),

])
def test_get_names(data, expected):
    result = list(map(lambda i: i["name"], data))
    expected = ['John', 'Marry', 'Mathew']
    assert result == expected
