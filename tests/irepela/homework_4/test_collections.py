import pytest

some_str = "abcd"
some_tuple = "a", "b", "c", "d"
some_list = ["a", "b", "c", "d"]
some_set = {"a", "b", "c", "d"}
some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}


@pytest.mark.parametrize("a, expected", [
    (some_str, 4),
    (some_tuple, 4),
    (some_list, 4),
    (some_set, 4),
    (some_dict, 4)
])
def test_collections_length(a, expected):
    assert len(a) == expected


@pytest.mark.parametrize("a, b, expected", [
    ("a", some_str, True),
    ("c", some_set, True),
    ("f", some_dict, False),
])
def test_collections_contains(a, b, expected):
    assert (a in b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (0, some_str, "a"),
    (3, some_tuple, "d"),
    (-1, some_list, "d"),
    ("d", some_dict, 100),
])
def test_collections_get_item(a, b, expected):
    assert b[a] == expected


@pytest.mark.parametrize("collection, expected", [
    (some_str, "a"),
    (some_tuple, "a"),
    (some_list, "a"),
])
def test_collections_unpacking(collection, expected):
    first, *tail = collection
    *head, last = collection
    assert first == expected
    assert tail == ["b", "c", "d"]
    assert head == ["a", "b", "c"]
    assert last == "d"


@pytest.mark.parametrize("collection, expected", [
    (some_str, "d"),
    (some_tuple, "d"),
    (some_list, "d"),
    (some_dict, "d")
])
def test_collections_sorting(collection, expected):
    result = sorted(collection, reverse=True)
    assert result[0] == expected


def test_collections_zip():
    result = list(zip(some_str, some_tuple, some_list))
    print(result)
    assert result[0] == ("a", "a", "a")
