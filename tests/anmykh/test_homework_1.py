import pytest


@pytest.mark.parametrize(["item", "data_type"], [
    ("sad", str)])
def test_is_string(item, data_type):
    assert isinstance(item, data_type)


@pytest.mark.parametrize(["item", "data_type"], (
    ({3, 2, "sad"}, set),
    (set(), set),
    ("abc", str)
))
def test_is_set(item, data_type):
    assert isinstance(item, data_type)


def test_split():
    a = "Hello World"
    b = a.split
    c = " "
    d = b(c)
    e = 0
    f = d[e]
    assert f == "Hello"
