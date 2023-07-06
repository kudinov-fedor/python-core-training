import pytest

from ahavryshkevych.task_set_cases import set_equality01, set_equality02, set_union, set_difference


@pytest.mark.parametrize(["arg1", "arg2", "res"], [
    ({"a", "b", "c"}, {"b", "a", "c"}, True),
    ({"a", "b", "c"}, {"a"}, False),
    ({"a", "c"}, {"b", "a", "c"}, False)
])
def test_set_equality01(arg1, arg2, res):
    assert set_equality01(arg1, arg2) == res


@pytest.mark.parametrize(["arg1", "arg2", "res"], [
    ({"a", "b", "c"}, {"b", "a", "c"}, False),
    ({"a", "b", "c"}, {"a"}, False),
    ({"a", "c"}, {"b", "a", "c"}, True)
])
def test_set_equality02(arg1, arg2, res):
    assert set_equality02(arg1, arg2) == res


@pytest.mark.parametrize(["arg1", "arg2", "res"], [
    ({"a", "b", "x"}, {"a", "x", "f"}, False),
    ({"a", "b", "c"}, {"a", "c", "b"}, False)
])
def test_set_union_check(arg1, arg2, res):
    assert set_union(arg1, arg2) == res


@pytest.mark.parametrize(["arg1", "arg2", "res"], [
    ({"a", "b", "x"}, {"a", "x", "f"}, set("b")),
    ({"a", "b", "x"}, {"a", "b", "f"}, set("x"))
])
def test_set_difference(arg1, arg2, res):
    assert set_difference(arg1, arg2) == res
