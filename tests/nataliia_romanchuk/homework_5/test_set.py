# SETS

some_set = {"a", "b", "c"}
some_set_2 = {"b", "a", "c"}


def test_is_container():
    assert len(some_set) == 3
    assert "a" in some_set
    assert list(sorted(some_set)) == ['a', 'b', 'c']


def test_is_subset1():
    assert some_set == some_set_2
    assert sorted(some_set) <= sorted(some_set_2)
    assert sorted(some_set_2) <= sorted(some_set)

    assert {"a"} < some_set
    # assert {"f"} < some_set           ##don't know how to test it
    assert {"a", "c"} < some_set
    assert some_set > {"a", "c"}


def test_is_subset2():
    assert {"a", "c"}.issubset({"a", "c", "b"})
    assert {"a", "c"}.issubset(["a", "b", "c"])
    assert {"a", "c"}.issubset("cab")


def test_superset():
    assert some_set.issuperset({"a", "c"})
    assert some_set.issuperset(["a", "c"])
    # assert some_set.issuperset(["ac"])  ##don't know how to test it


def test_union():
    union1 = {"a", "b", "x"} | {"a", "x", "f"}
    assert union1 == {'f', 'a', 'b', 'x'}

    union2 = {"a", "b", "x"}.union({"a", "x", "f"})
    assert union2 == {'f', 'a', 'b', 'x'}


def test_update():
    a = {"a", "b", "c"}
    a |= {"b", "x", "d"}
    assert a == {'a', 'b', 'd', 'x', 'c'}

    a.update({"f", "x", "k"})
    assert a == {'f', 'a', 'k', 'd', 'b', 'x', 'c'}

    a.update("safz")
    assert a == {'b', 'x', 'z', 'a', 'd', 's', 'c', 'f', 'k'}

    a.update(["r", "e", "z"])
    assert a == {'b', 'x', 'z', 'r', 'a', 'd', 's', 'c', 'f', 'k', 'e', 'z'}


def test_diff():
    a = {"a", "b", "x"} - {"a", "x", "f"}
    assert a == {'b'}

    b = {"a", "b", "x"}.difference({"a", "x", "f"})
    assert b == {'b'}


def test_symetric_diff():
    a = {"a", "b", "x"} ^ {"a", "x", "f"}
    assert a == {'f', 'b'}

    b = {"a", "b", "x"}.symmetric_difference({"a", "x", "f"})
    assert b == {'f', 'b'}


def test_intersection():
    a = {"a", "b", "x"} & {"a", "x", "f"}
    assert a == {'a', 'x'}

    b = {"a", "b", "x"}.intersection({"a", "x", "f"})
    assert b == {'a', 'x'}
