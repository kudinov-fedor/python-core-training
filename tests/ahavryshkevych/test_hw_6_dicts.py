import pytest
from ahavryshkevych.task_dict_cases import dict_comparison, dict_compr_convert, dict_gender_check, dict_value_change

data = {"age": 16, "name": "John", "sex": "M"}


@pytest.mark.parametrize(["arg1", "arg2", "res"], [
    ({"a": 123, "b": 456, "c": 789}, {"c": 789, "a": 123, "b": 456}, True),
    ({"D": 123, "b": 456, "c": 789}, {"c": 789, "a": 123, "b": 456}, False)
])
def test_dict_comparison(arg1, arg2, res):
    assert dict_comparison(arg1, arg2) == res


@pytest.mark.parametrize(["arg1", "res"], [
    ({"a": 123, "b": 456, "c": 789}, True)
])
def test_dict_convert(arg1, res):
    assert dict_compr_convert(arg1) == res


@pytest.mark.parametrize(["agr", "res"], [
    ([{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
      {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
      {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
      {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"},
      {"age": 25, "second_name": "Baton", "name": "Mathew", "sex": "M"}
      ], True)
])
def test_grouping_by_key(agr, res):
    assert dict_gender_check(agr) == res


@pytest.mark.parametrize(["arg1", "res"], [
    (data["name"], "John"),
    (data["age"], 16),
    (data["sex"], "M")
])
def test_check_key_value(arg1, res):
    assert arg1 == res


@pytest.mark.parametrize(["arg1", "arg2", "arg3", "res"], [
    (data, "age", 25, 25),
    (data, "name", "Mila", "Mila"),
    (data, "sex", "F", "F")
])
def test_check_value_change(arg1, arg2, arg3, res):
    assert dict_value_change(arg1, arg2, arg3) == res
