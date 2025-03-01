import pytest


def test_list_compr():
    fruits = ["apple", "banana", "blackberry", "kiwi", "cherry", "pear", "coconut"]
    new_list = [x for x in fruits if "a" in x]
    assert new_list == ["apple", "banana", "blackberry", "pear"]


def test_call_len_func_in_list_compr():
    fruits = ["apple", "banana", "blackberry", "kiwi", "cherry", "pear", "coconut"]
    new_list = [len(x) for x in fruits]
    assert new_list == [5, 6, 10, 4, 6, 4, 7]


def test_two_conditions_in_list_compr():
    new_list = [x for x in range(12) if x < 7]
    assert new_list == [0, 1, 2, 3, 4, 5, 6]


def test_zero_division_error_in_list_compr():
    a = [1, 3, 0, 44, 12]
    with pytest.raises(ZeroDivisionError):
        [1 / x for x in a]


def test_value_error_in__list_compr():
    a = [1, 2.3, 16.33, 'aaa', 12, 1]
    with pytest.raises(ValueError):
        [int(x) for x in a]


def test_name_error_in_list_compr():
    a = [1, 2, 3, 4, 5]
    with pytest.raises(NameError):
        [x + 1 for y in a]


def test_if_condition_in_list_compr():
    a = [1, 33, 4.5, "ddd", 4, "56", False, -66, None]
    new_list = ["int" if isinstance(x, int) else "non int" for x in a]
    assert new_list == ['int', 'int', 'non int', 'non int', 'int', 'non int', 'int', 'int', 'non int']


def test_empty_result_for_list_compr():
    new_list = [x for x in []]
    assert new_list == []


def test_iteration_with_zero_elements_in_list_compr():
    new_list = [x + 1 for x in range(0)]
    assert new_list == []


def test_nested_loops_in__list_compr():
    new_list = [(x, y) for x in range(3) for y in range(2)]
    assert new_list == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


def test_convert_types_in__list_compr():
    a = [1, 2.45, "test", True, -66]
    new_list = [str(x) for x in a]
    assert new_list == ['1', '2.45', 'test', 'True', '-66']


def test_set_with_comprehensions():
    new_set = {x ** 2 for x in range(2, 5)}
    assert new_set == {16, 9, 4}


def test_dict_with_comprehensions():
    new_dict = {x: "value = "+str(x) for x in range(3)}
    assert new_dict == {0: 'value = 0', 1: 'value = 1', 2: 'value = 2'}


def test_logical_operators_in_list_compr():
    a = [1, 12, 2.3, 17, -4, 6, 22, 0]
    new_list = [x for x in a if x % 2 == 0 and x > 6]
    assert new_list == [12, 22]
