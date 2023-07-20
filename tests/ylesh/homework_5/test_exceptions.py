import pytest


def error_func():
    5 / 0


def error_func_2():
    a = []
    a[0]


def error_func_3():
    x


def error_func_4():
    import invalid


def error_func_5():
    1 + "123"


def error_func_6():
    a = []
    a.invalid


def error_func_7():
    eval("x = ")


def error_func_8():
    error_func_8()


def test_errors():
    with pytest.raises(ZeroDivisionError):
        error_func()
    with pytest.raises(IndexError):
        error_func_2()
    with pytest.raises(NameError):
        error_func_3()
    with pytest.raises(ModuleNotFoundError):
        error_func_4()
    with pytest.raises(TypeError):
        error_func_5()
    with pytest.raises(AttributeError):
        error_func_6()
    with pytest.raises(SyntaxError):
        error_func_7()
    with pytest.raises(RecursionError):
        error_func_8()


def func_1(a):
    a / 0


def func_2(a):
    func_1(a)


def func_3(a):
    func_2(a)


def main_func(a):
    func_3(a)


def test_errors_2():
    with pytest.raises(ZeroDivisionError):
        main_func(5)
