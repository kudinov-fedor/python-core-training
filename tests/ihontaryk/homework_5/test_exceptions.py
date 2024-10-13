import pytest

from ihontaryk.homework_5.exceptions import *


@pytest.mark.parametrize('function, error',
                         [(error_func, ZeroDivisionError),
                          (error_func_2, IndexError),
                          (error_func_3, NameError),
                          (error_func_4, ModuleNotFoundError),
                          (error_func_5, TypeError),
                          (error_func_6, AttributeError),
                          (error_func_7, TypeError),
                          (error_func_8, TypeError),
                          (error_func_9, SyntaxError),
                          (error_func_10, RecursionError),
                          (func_1, ZeroDivisionError),
                          (func_2, ZeroDivisionError),
                          (func_3, ZeroDivisionError),
                          (main_func, ZeroDivisionError)
                          ])
def test_exceptions(function, error):
    """
    verify raising exceptions for functions
    """

    with pytest.raises(error):
        function()
