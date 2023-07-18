import pytest
from mizo.task_group_dictionary import group_dictionary

some_dict = {"a": 123, "b": 456, "c": 789}


def test_some_dict():
    expected = {"a": 123, "b": 456, "c": 789}
    assert some_dict == expected
    assert len(some_dict) == 3


def test_set_default():
    some = {"a": 1, "b": 2}
    item = some.pop("a")
    item = some.setdefault("a", 5)
    key_exists = "a" in some
    assert key_exists is True
    assert item == 5


def test_dict_comprehension():
    assert {k * 2: str(v) for k, v in some_dict.items()} == {"aa": "123", "bb": "456", "cc": "789"}


data = [
    {"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
    {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
    {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
    {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}
]


@pytest.mark.parametrize("data_input, expected_output", [
    (
            data,
            {
                "M": [
                    {"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
                    {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}
                ],
                "F": [
                    {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
                    {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"}
                ]
            }
    )
])
def test_group_dictionary(data_input, expected_output):
    result = group_dictionary(data_input)
    assert result == expected_output
