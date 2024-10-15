some_set = {"a", "b", "c"}
some_set_2 = {"b", "a", "c"}


def test_sets_compare():
    assert some_set == some_set_2
    assert some_set is not some_set_2
    assert {"a"} < some_set


def test_subset_superset():
    assert {"a", "c"}.issubset(some_set)
    assert some_set.issuperset({"a", "c"})


def test_set_union():
    assert some_set.union(some_set_2) == some_set
    assert {"a", "b", "x"}.union({"a", "x", "f"}) == {"a", "b", "x", "f"}


def test_set_difference():
    assert {"a", "b", "x"}.difference({"a", "x", "f"}) == {"b"}
    assert {"a", "b", "x"}.symmetric_difference({"a", "x", "f"}) == {"b", "f"}


def test_set_intersection():
    assert {"a", "b", "x"}.intersection({"a", "x", "f"}) == {"a", "x"}
