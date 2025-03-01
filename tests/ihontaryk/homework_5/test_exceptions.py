import pytest

from ihontaryk.homework_5 import exceptions as e


@pytest.mark.parametrize('function, error',
                         [(e.error_func, ZeroDivisionError),
                          (e.error_func_2, IndexError),
                          (e.error_func_3, NameError),
                          (e.error_func_4, ModuleNotFoundError),
                          (e.error_func_5, TypeError),
                          (e.error_func_6, AttributeError),
                          (e.error_func_7, TypeError),
                          (e.error_func_8, TypeError),
                          (e.error_func_9, SyntaxError),
                          (e.error_func_10, RecursionError),
                          (e.func_1, ZeroDivisionError),
                          (e.func_2, ZeroDivisionError),
                          (e.func_3, ZeroDivisionError),
                          (e.main_func, ZeroDivisionError)
                          ])
def test_exceptions(function, error):
    """
    verify raising exceptions for functions
    """

    with pytest.raises(error):
        function()
