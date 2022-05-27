import pytest


@pytest.mark.skip
def test_append(test_list):
    test_list.append(4)
    assert test_list == [1, 2, 3, 4]


def test_extend(test_list):
    if not isinstance(test_list, list):
        pytest.skip(reason='test_list is not a list')
    test_list.extend([4, 5])
    assert test_list == [1, 2, 3, 4, 5]


def test_insert(test_list):
    test_list.insert(1, 'X')
    assert test_list == [1, 'X', 2, 3]
