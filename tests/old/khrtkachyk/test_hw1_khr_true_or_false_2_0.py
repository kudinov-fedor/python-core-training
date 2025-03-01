import pytest


@pytest.mark.parametrize(["par1", "res"], [
    ((lambda: any(["", 0, False, (), None])), False),
    ((lambda: any(["", 0, False, (1,), None])), True),
    # ((lambda: bool({})), False),
])
def test_at_least_1_true(par1, res):
    assert par1() is res


@pytest.mark.parametrize(["par2", "res2"], [
    ((lambda: bool(1 and "abc" and 0.0 and "some value")), False),
    ((lambda: bool(None or 0 or "" or [] or {})), False),
    ((lambda: bool("some" and {})), False)
])
def test_take_first_or_last(par2, res2):
    assert par2() is res2


@pytest.mark.parametrize(["par3", "res3"], [
    ((lambda: check_data(item=resulting)), ['cat', 'dog', 1, -2, True])
])
def test_check_data(par3, res3):
    assert par3() == res3


def check_data(item):
    if item is not False:
        return item


data = ["cat", "dog", "", None, False, 0, 1, -2, True]
resulting = list(filter(check_data, data))
