import pytest

from ppyze.homework_collections import first_and_last_upper_only_string, unpacking_first_and_last_only_tuple, \
    operations_on_list, operations_on_set, operations_on_dict


@pytest.mark.parametrize('text, expected', [
    ('Alamakota', 'AlamakotA'),
    ('aLaMaKoTa', 'AlamakotA'),
    ('A', 'A'),
    ('AlamakotA', 'AlamakotA')
])
def test_first_and_last_upper_only_string(text, expected):
    """
    data driven test
    """
    assert first_and_last_upper_only_string(text) == expected


@pytest.mark.parametrize('tpl, expected', [
    ((1, 2, 3, 4, 5, 6,), (1, 6)),
    ('abcdefg', ('a', 'g')),
])
def test_unpacking_first_and_last_only_tuple(tpl, expected):
    assert unpacking_first_and_last_only_tuple(tpl) == expected


@pytest.mark.parametrize('lst, expected', [
    ([1,2,3], [1,2,3,1,2,3,1,1,2,3,1,2,3,1]),
])
def test_operations_on_list(lst, expected):
    assert repr(operations_on_list(lst)) == repr(expected)


@pytest.mark.parametrize('st, expected', [
    ({1,2,3,4}, {1,2,3,4}),
    ({6,7}, {1}),
    ({4}, {1,4})
])
def test_operations_on_set(st, expected):
    assert operations_on_set(st) == expected


@pytest.mark.parametrize('st, expected', [
    ({1:2, 2:3}, {1:1, 2:3}),
    ({2:3,3:4}, {1:1, 2:3, 3:4})
])
def test_operations_on_dict(st, expected):
    assert operations_on_dict(st) == expected





