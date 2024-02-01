import pytest


@pytest.mark.parametrize(["item", "data_type"],
                         [("sad", str)])
def test_is_string(item, data_type):
    assert isinstance(item, data_type)


@pytest.mark.parametrize(["item", "data_type"],
                         [({3, 2, "sad"}, set)])
def test_is_set(item, data_type):
    assert isinstance(item, data_type)


@pytest.mark.parametrize(["item", "data_type"],
                        [(12, tuple)])
def test_is_tuple(item, data_type):
    assert type(item) is not tuple


@pytest.mark.parametrize(["item", "spliter", "number"],
                         [("Hello World", " ", 0)])
def test_split(item, spliter, number):
    a = item
    b = a.split
    c = spliter
    d = b(c)
    e = number
    f = d[e]
    assert f == "Hello"
