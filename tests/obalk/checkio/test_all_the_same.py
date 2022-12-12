import pytest

from obalk.checkio.all_the_same import all_the_same, all_the_same_set


@pytest.mark.parametrize("function", [
    all_the_same,
    all_the_same_set
])
@pytest.mark.parametrize("elements, result", [
    ([], True),
    ([1], True),
    ([1, 'a', 1], False),
    ([1, 1, 1], True),
    ([1, 2, 1], False),
])
def test_all_the_same(function, elements, result):
    assert function(elements) == result
