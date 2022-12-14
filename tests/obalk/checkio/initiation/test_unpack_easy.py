import pytest

from obalk.checkio.initiation.unpack_easy import easy_unpack


@pytest.mark.parametrize("elements, result", [
    ((1, 2, 3, 4, 5, 6, 7, 9), (1, 3, 7)),
    ((1, 1, 1, 1), (1, 1, 1)),
    ((6, 3, 7), (6, 7, 3))
])
def test_easy_unpack(elements, result):
    assert easy_unpack(elements) == result
