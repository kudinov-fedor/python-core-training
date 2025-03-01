import pytest


def error_func_1():
    a = []
    a[0]


def test_error_func_1():
    with pytest.raises(IndexError):
        error_func_1()


def error_func_2():
    import something


def test_error_func_2():
    with pytest.raises(ImportError):
        error_func_2()


def error_func_3():
    res = ["d", "o", "g"] <= ["d", "a", "y"]
    assert res is True


def test_error_func_3():
    with pytest.raises(AssertionError):
        error_func_3()
