import pytest

some_str = "fabcdefdgab"
some_list = [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
some_tuple = (1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4)


@pytest.mark.parametrize("a, b, expected", [
    ("a", some_str, 2),
    (5, some_list, 2),
    (6, some_tuple, 1),
])
def test_list_count(a, b, expected):
    assert b.count(a) == expected


@pytest.mark.parametrize("a, b, expected", [
    ("c", some_str, 3),
    (6, some_list, 5),
    (6, some_tuple, 5),
])
def test_list_index(a, b, expected):
    assert b.index(a) == expected


def test_list_extend():
    list_copy = list(some_list)
    list_copy.extend([7, 8, 9])
    assert list_copy == [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4, 7, 8, 9]
    assert some_list == [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
