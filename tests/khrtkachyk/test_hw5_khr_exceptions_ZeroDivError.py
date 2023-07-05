import pytest

def func_1():
    5 / 0


def func_2():
    func_1()


def func_3():
    func_2()


def main_func():
    func_3()


def test_zero_div_error1_0():
    with pytest.raises(ZeroDivisionError):
        main_func()


def test_zero_div_error2_0():
    with pytest.raises(Exception):
        main_func()


def test_zero_div_error3_0():
    with pytest.raises(ArithmeticError):
        main_func()


def test_zero_div_error4_0():
    with pytest.raises(ZeroDivisionError):
        func_3()


def test_zero_div_error5_0():
    with pytest.raises(Exception):
        func_2()


def test_zero_div_error6_0():
    with pytest.raises(ArithmeticError):
        func_1()
