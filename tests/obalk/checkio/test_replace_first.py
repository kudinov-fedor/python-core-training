import pytest

from obalk.checkio.replace_first import replace_first, replace_first_slice


@pytest.mark.parametrize("function", [
    replace_first,
    replace_first_slice
])
@pytest.mark.parametrize("items, result", [
    ([], []),
    ([1], [1]),
    ([10], [10]),
    ([1, 2, 3, 4], [2, 3, 4, 1]),
    ([1, 0, 2, 3], [0, 2, 3, 1]),

])
def test_replace_first(function, items, result):
    assert function(items.copy()) == result
