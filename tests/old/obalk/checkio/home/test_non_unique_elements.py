import pytest

from obalk.checkio.home.non_unique_elements import non_unique_elements


@pytest.mark.parametrize("numbers, result", [
    ([1, 2, 3, 4, 5], []),
    ([1, 2, 3, 1, 3], [1, 3, 1, 3]),
    ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5])
])
def test_non_unique_elements(numbers, result):
    assert non_unique_elements(numbers) == result
