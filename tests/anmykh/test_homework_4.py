import pytest


@pytest.mark.parametrize(["a", "b"], [
    ([1, 2, 3, 4], 53)
])
def test_modify_collection(a, b):
    a[3] = b
    assert a[3] == b


@pytest.mark.parametrize(["param", "result"],
                         [("abcd", 4)])
def test_length_collection(param, result):
    assert len(param) == result


@pytest.mark.parametrize(["item", "option"],
                         [({"a": 123, "b": 456}, 7889)])
def test_modify_collection2(item, option):
    item["c"] = option
    assert item["c"] == option


@pytest.mark.parametrize(["item", "result"],
                         [("abcd", ["a", "b", "c", "d"])])
def test_unpack_collection(item, result):
    assert list(item) == result
