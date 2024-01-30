import pytest


@pytest.mark.parametrize("collection", [
    "asdf",
    [1, 2, 3, 4],
    {"y", "e", "a", "r"},
    ('h', 'e', 'l', 'p'),
    {'a': 1, 's': 2, 'd': 3, 'f': 4}
])
def test_len(collection):
    assert len(collection) == 4


@pytest.mark.parametrize("collection, res", [
   ["hello world", 3],
   [["h", "e", "l", "l", "o"], 2],
   [('t', 'e', 's', 't'), 0],
])
def test_count(collection, res):
    assert collection.count('l') == res


@pytest.mark.parametrize("collection, multiplier, res", [
    ["cat", 3, "catcatcat"],
    [("c", "a", "t"), 2, ('c', 'a', 't', 'c', 'a', 't')],
    [["c", "a", "t"], 0, []],
])
def test_multiplication(collection, multiplier, res):
    assert collection * multiplier == res


@pytest.mark.parametrize("collection, separator, res", [
    ["banana, tomatoes, apples", ", ", ['banana', 'tomatoes', 'apples']],
    ["This Is My Way", " ", ['This', 'Is', 'My', 'Way']],
])
def test_split(collection, separator, res):
    assert collection.split(separator) == res

