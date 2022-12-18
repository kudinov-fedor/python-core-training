import pytest

from obalk.checkio.home.duplicate_zeros import duplicate_zeros


@pytest.mark.parametrize("elements, result", [
    ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]),
    ([0], [0, 0]),
    ([1, 2, 3], [1, 2, 3])
])
def test_duplicate_zeros(elements, result):
    assert duplicate_zeros(elements) == result
