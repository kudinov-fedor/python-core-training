import pytest
from mizo.task_introspection import filter_even_numbers
from mizo.task_introspection import my_name_length


@pytest.mark.parametrize("my_list, expected", [
    ([1, 3, 4, 6, 10, 11, 15, 12, 14], [4, 6, 10, 12, 14]),
    ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10]),
    ([1, 3, 5, 7, 9], []),
    ([], []),
])
def test_filtered_list(my_list, expected):
    assert filter_even_numbers(my_list) == expected


def test_len():
    assert len(my_name_length()) == 8
