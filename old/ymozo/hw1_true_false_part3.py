import pytest


@pytest.mark.parametrize(["par1", "expected"], [
    (bool(None), False),
    (bool(False), False),
    (bool(0), False),
    (bool(0.0), False),
    (bool(""), False),
    (bool([]), False),
    (bool(()), False),
    (bool({}), False),
    (bool(set()), False),
    (bool(True), True),
    (bool(3), True),
    (bool(-0.1), True)
])
def test_bool_values(par1, expected):
    result = par1
    assert result == expected


@pytest.mark.parametrize(["par1", "expected"], [
    (bool("abc"), True),
    (bool([False, ]), True),
    (bool((None,)), True),
    (bool({"a": 123}), True),
    (bool({1, "abc"}), True),
    (not 5, False),
    (not 0, True),
    (not True, False),
    (not False, True),
    (not [], True),
    (not (1, 2, 3), False)
])
def test_check_bool_containers(par1, expected):
    result = par1
    assert result == expected


@pytest.mark.parametrize(["par1", "expected"], [
    (len("abc"), True),
    (len([False, ]), True),
    (len((None,)), True),
    (len({"a": 123}), True),
    (len({1, "abc"}), True)
])
def test_check_bool_containers_1(par1, expected):
    result = par1 > 0
    assert result == expected


def test_check_comparison():
    a = "it is true" if True else "it is false"
    result = "it is true"
    assert a == result


def test_check_comparison_1():
    a = "it is true" if False else "it is false"
    result = "it is false"
    assert a == result


def test_check_comparison_2():
    a = "it is true" if "abc" else "it is false"
    result = "it is true"
    assert a == result


def test_check_comparison_3():
    a = "it is true" if "" else "it is false"
    result = "it is false"
    assert a == result


def test_check_comparison_4():
    a = "it is true" if [] else "it is false"  # as list is empty it return false
    result = "it is false"
    assert a == result


def test_check_comparison_5():
    a = "it is true" if [None] else "it is false"  # as list is not empty it return true
    result = "it is true"
    assert a == result


@pytest.mark.parametrize(["par1", "par2", "expected"], [
    (True, False, True),
    (False, True, True),
    (1, 3, 1),
    ([], "abc", "abc"),
    (None, "some", "some"),
])
def test_check_first_item_true_or_last(par1, par2, expected):
    result = par1 or par2
    assert result == expected


def test_check_first_item_true_or_last_1():
    result = None or 0 or "" or [] or "at last some value"
    expected = "at last some value"
    assert result == expected


def test_check_first_item_true_or_last_2():
    result = None or 0 or "" or [] or {}
    expected = {}
    assert result == expected


@pytest.mark.parametrize(["par1", "par2", "expected"], [
    (True, False, False),
    (False, True, False),
    (1, 3, 3),
    ([1, 2, 3], "abc", "abc"),
    ("some", {}, {})
])
def test_check_first_item_true_or_last_3(par1, par2, expected):
    result = par1 and par2
    assert result == expected


def test_check_first_item_true_or_last_4():
    result = 1 and "abc" and 0.0 and "some value"
    expected = 0.0
    assert result == expected


@pytest.mark.parametrize(["par1", "par2", "par3", "expected"], [
    ("", "Some", {}, {}),
    (False, "", 123, "")
])
def test_check_priority(par1, par2, par3, expected):
    result = par1 or par2 and par3
    assert result == expected


@pytest.mark.parametrize(["par1", "expected"], [
    ((all(["a", 0, True, (1, 2, 3)])), False),
    ((all(["a", -1, True, (1, 2, 3)])), True),
    ((all(["a", -1, False, (1, 2, 3)])), False),
    ((all(["a", -1, True, ()])), False)
])
def test_check_if_all_true(par1, expected):
    result = par1
    assert result == expected


@pytest.mark.parametrize(["par1", "expected"], [
    (any(["", 0, False, (), None]), False),
    (any(["", 1, False, (), None]), True),
    (any(["", 0, True, (), None]), True),
    (any(["", 0, False, (1,), None]), True)
])
def test_check_if_any_true(par1, expected):
    result = par1
    assert result == expected


def test_check_filter_1():
    data = ["cat", "dog", "", None, False, 0, 1, -2, True]
    result = list(filter(None, data))
    expected = ["cat", "dog", 1, -2, True]
    assert result == expected


def test_check_filter_2():
    data = ["cat", "dog", "", None, False, 0, 1, -2, True]
    result = list(filter(lambda i: isinstance(i, str), data))
    expected = ["cat", "dog", ""]
    assert result == expected