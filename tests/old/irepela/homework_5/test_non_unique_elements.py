import pytest
from irepela.homework_5.non_unique_elements import non_unique_elements


@pytest.mark.parametrize("a, expected", [
    ([1, 2, 3, 1, 3], [1, 3, 1, 3]),
    ([1, 2, 3, 4, 5], []),
    ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
    ([10, 9, 10, 10, 9, 8], [10, 9, 10, 10, 9]),
    ([0, 0, 0, -1, -1, 100], [0, 0, 0, -1, -1]),
    ([7], [])

])
def test_non_unique_elements(a, expected):
    assert non_unique_elements(a) == expected
