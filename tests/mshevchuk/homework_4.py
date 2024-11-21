import pytest


@pytest.mark.parametrize("collection", [
    (1, 2, 3, 4),
    "abcd",
    [1, 2, 3, 4],
    {1, 2, 3, 2, 3, 1, 1, 1, 2, 4},
    {"a": 1, "b": 2, "a": 4, "c": 3, "d": 3}
])
def test_len(collection):
    assert len(collection) == 4


@pytest.mark.parametrize("collection", [
    (1, 2, 3, 4, "a"),
    "abcd",
    [1, 2, 3, 4, "a"],
    {1, 2, 3, 2, 3, 1, 1, 1, 2, 4, "a"},
    {"a": 1, "b": 2, "a": 4, "c": 3, "d": 3}
])
def test_in_collection(collection):
    assert "a" in collection
