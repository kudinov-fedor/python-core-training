import pytest
import homework.homework_5.exceptions as hw_fun


#  was it possible here to write one test for all exception and just send different functions as parameters?
def test_division_zero():
    with pytest.raises(Exception) as e_info:
        hw_fun.error_func()
    assert "division by zero" in str(e_info.value)


def test_division_zero2():
    with pytest.raises(Exception) as e_info:
        hw_fun.main_func()
    assert "division by zero" in str(e_info.value)


def test_index_error():
    with pytest.raises(Exception) as e_info:
        hw_fun.error_func_2()
    assert "index out of range" in str(e_info.value)


def test_unsupported_operand():
    with pytest.raises(Exception) as e_info:
        hw_fun.error_func_5()
    assert "unsupported operand" in str(e_info.value)


def test_invalid_syntax():
    with pytest.raises(Exception) as e_info:
        hw_fun.error_func_9()
    assert "invalid syntax" in str(e_info.value)