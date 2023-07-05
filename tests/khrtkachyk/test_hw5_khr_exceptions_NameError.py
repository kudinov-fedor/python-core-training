import pytest


def func_2():
    func_1()


def func_3():
    func_2()


def main_func():
    func_3()



def test_main_func():
    with pytest.raises(NameError):
        main_func()


def test_exception():
    try:
        main_func()
        assert False
    except Exception:
        assert True
