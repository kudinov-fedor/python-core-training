import pytest

some_set = {"a", "b", "c"}
some_set_2 = {"b", "a", "c"}


def test_check_converting_to_list():
    new_list = sorted(list(some_set))
    expected_list = ["a", "b", "c"]
    assert new_list == expected_list


def test_subset_1():
    assert {"a", "c"}.issubset({"a", "c", "b"})
    assert not some_set.issuperset(["ac"])


def test_subset_2():
    assert {"a", "c"}.issubset(["a", "b", "c"]) == True


def test_superset_1():
    assert some_set.issuperset({"a", "c"}) == True


def test_superset_2():
    assert some_set.issuperset(["a", "c"]) == True


def test_superset_3():
    assert some_set.issuperset(["ac"]) == False


def test_union_1():
    new_set = {"a", "b", "x"} | {"a", "x", "f"}
    assert new_set == {"a", "x", "b", "f"}


def test_update_1():
    a = {"a", "b", "c"}
    a.update({"f", "x", "k"})
    assert a == {"a", "b", "c", "f", "x", "k"}


def test_update_2():
    a = {"a", "b", "c"}
    a.update("safz")
    assert a == {"a", "b", "c", "s", "a", "f", "z"}


def test_update_3():
    a = {"a", "b", "c"}
    a.update(["r", "e" "z"])
    assert a == {"a", "b", "c", "r", "e" "z"}


def test_difference():
    modif_set = {"a", "b", "c"}.difference({"a", "x", "f"})
    assert modif_set == {"b", "c"}


def test_check_symetric_dif():
    symetric_diff = {"a", "b", "x"} ^ {"a", "x", "f"}
    assert symetric_diff == {"b", "f"}


def test_intersection():
    modif_set = {"a", "b", "x"}.intersection({"a", "x", "f"})
    assert modif_set == {"a", "x"}
