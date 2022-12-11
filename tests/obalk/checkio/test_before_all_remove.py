import pytest

from obalk.checkio.before_all_remove import remove_all_before, remove_all_before_boolean


@pytest.mark.parametrize("function", [
    remove_all_before,
    remove_all_before_boolean
])
@pytest.mark.parametrize("items, border, result", [
    ([], 1, []),
    ([2], 1, [2]),
    ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
    ([1, 1, 2, 2, 3], 2, [2, 2, 3]),
])
def test_remove_all_before(function, items, border, result):
    assert function(items, border) == result
