import pytest


@pytest.mark.parametrize(['values_list', 'expected'], [
    (["", 0, True, (), {}, None], ["", 0, (), {}, None]),
])
def test_find_any(values_list, expected):
    values_list.remove(any(values_list))
    assert values_list == expected


@pytest.mark.parametrize(['values_list', 'expected'], [
    (["", 0, True, (), {}, None, 1], [True, 1]),
])
def test_none_filter_in_list(values_list, expected):
    assert list(filter(None, values_list)) == expected


@pytest.mark.parametrize(['values_list', 'arg', 'expected'], [
    (["cat", "dog", "", None, False, 0, 1, -2, True], str, ["cat", "dog", ""]),
    (["cat", "dog", "", None, False, 0, 1, -2, True], bool, [False, True]),
    (["cat", "dog", "", None, False, 0, 1, -2, True], int, [False, 0, 1, -2, True]),
    (["cat", "dog", "", None, False, 0, 1, -2, True, 0.007], float, [0.007])
])
def test_obj_type_filter_in_list(values_list, arg, expected):
    assert list(filter(lambda i: isinstance(i, arg), values_list)) == expected


@pytest.mark.parametrize(['values_list', 'expected'], [
    (["a", -1, 0, (1, 2, 3)], False),
    (["a", -1, True, (1, 2, 3)], True),
    (["a", -1, ()], False)
])
def test_all_true_values_in_list(values_list, expected):
    assert all(values_list) is expected
