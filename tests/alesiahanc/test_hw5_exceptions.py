import pytest
import homework.homework_5.exceptions as hw_fun


@pytest.mark.parametrize(["func", "expected_exception", "msg"], [
    (hw_fun.main_func, Exception, "division by zero"),
    (hw_fun.error_func, Exception, "division by zero"),
    (hw_fun.error_func_3, NameError, "is not defined"),
    (hw_fun.error_func_4, ModuleNotFoundError, "No module named")
])
def test_catch_exceptions(func, expected_exception, msg):
    with pytest.raises(expected_exception, match=msg):
        func()


def test_division_zero():
    with pytest.raises(Exception, match="division by zero"):
        hw_fun.main_func()


def test_index_error():
    with pytest.raises(Exception, match="index out of range"):
        hw_fun.error_func_2()


def test_unsupported_operand():
    with pytest.raises(Exception, match="unsupported operand"):
        hw_fun.error_func_5()


def test_invalid_syntax():
    with pytest.raises(Exception, match="invalid syntax"):
        hw_fun.error_func_9()
