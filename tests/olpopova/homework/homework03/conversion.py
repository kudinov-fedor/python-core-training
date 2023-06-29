import pytest


def convert_list(list1, list2):
    return list(zip(list1, list2))


def convert_list2(list1, list2):
    return list(dict(enumerate(list2, start=list1[0])).items())


@pytest.mark.parametrize(['list1', 'list2', 'expected'], [
    ([7, 8, 9], ["a", "b", "c"], [(7, "a"), (8, "b"), (9, "c")])
])
def test_compare_tuples(list1, list2, expected):
    assert convert_list(list1, list2) == convert_list2(list1, list2) == expected
