import pytest

from obalk.checkio.home.changing_direction import changing_direction, changing_direction_zip


@pytest.mark.parametrize("function", [
    changing_direction,
    changing_direction_zip
])
@pytest.mark.parametrize("elements, result", [
    ([], 0),
    ([1], 0),
    ([5, 4, 9, 10, 10, 10, 10, 3, 8, 5, 1, 9, 9, 4, 1], 6),
    ([1, 2, 2, 1, 2, 1, 2], 4)
])
def test_changing_direction(function, elements, result):
    assert function(elements) == result
