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


@pytest.mark.parametrize("param", [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4],
    [2, 4, 5, 2]
    ])
def test_unpack_generator(param):
    assert list(i for i in param) == param


@pytest.mark.parametrize("param", [
    "abcdksemdsej",
    "bfjkgjna",
    "urhfanvjm",
    "jdbvncnzhbdsebjsfyvsefsbfthnkynhkjftjgnfhtgjhftga"
])
def test_a_in_string(param):
    assert param.count("a") > 0


@pytest.mark.parametrize("param", [
    [2, 3, 6, 7, 4],
    [0, 0, 0, 0],
    ["abc", "cds", "ssa"],
    ["a", "b", "c"]
])
def test_is_list_copy(param):
    assert param.copy() == param
    assert param.copy() is not param


@pytest.mark.parametrize("param", [
    [2, 3, 6, 7],
    [0, 0, 0, 0],
    [2, 4, 5, 6],
    [4, 6, 7, 3]
])
def test_append_list(param):
    new_list = param.copy()
    assert new_list.append(0) != new_list
