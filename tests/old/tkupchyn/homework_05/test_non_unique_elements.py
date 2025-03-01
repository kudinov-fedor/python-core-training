import pytest
from tkupchyn.homework_05.non_unique_elements import remove_unique_values


@pytest.mark.parametrize("list_with_interegrs, expected_result",
                         [
                             ([1, 2, 3, 1, 3], [1, 3, 1, 3]),
                             ([1, 2, 3, 4, 5], []),
                             ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
                             ([10, 9, 10, 10, 9, 8], [10, 9, 10, 10, 9])
                         ])
def test_remove_unique_values(list_with_interegrs, expected_result):
    assert list(remove_unique_values(list_with_interegrs)) == expected_result
