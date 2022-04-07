import pytest

from ylond.the_most_frequent_str import most_frequent


@pytest.mark.parametrize("a, expected", [
    (["a", "a", "b", "b", "c", "a"], "a"),
    ([1, 22, 22, 1, 100, 100], 1),
    (["A", "A", "a", "a"], "A")
])
def test_most_frequent(a, expected):
    assert most_frequent(a) == expected
