import pytest

from types import *

from homework.homework_3.introspection import *


@pytest.mark.parametrize("test_object, expected_result",
                         [(some_bool, bool),
                          (some_int, int),
                          (some_float, float),
                          (some_str, str),
                          (some_tuple, tuple),
                          (some_list, list),
                          (some_range, range),
                          (some_set, set),
                          (some_dict, dict),
                          (some_lambda, LambdaType),
                          (some_gen_func, FunctionType),
                          (some_func, FunctionType),
                          (some_object, SomeClass),
                          (some_error, ZeroDivisionError)
                          ])
def test_types(test_object, expected_result):
    """
    verify types of some objects
    """

    assert type(test_object) is expected_result


@pytest.mark.parametrize("test_object, expected_result",
                         [(some_bool, bool),
                          (some_bool, (int, float, str)),
                          (some_bool, object),
                          (some_int, int),
                          (some_float, float),
                          (some_str, str),
                          (some_tuple, tuple),
                          (some_list, list),
                          (some_range, range),
                          (some_set, set),
                          (some_dict, dict),
                          (some_lambda, LambdaType),
                          (some_gen_func, FunctionType),
                          (some_func, FunctionType),
                          (some_object, SomeClass),
                          (some_error, ZeroDivisionError),
                          (some_error, Exception),
                          (bool, type),
                          (bool, object)
                          ])
def test_instance(test_object, expected_result):
    """
    verify some objects is instance of class
    """

    assert isinstance(test_object, expected_result)


@pytest.mark.parametrize("test_object, expected_result",
                         [(bool, bool),
                          (bool, int),
                          (ZeroDivisionError, ArithmeticError),
                          (ZeroDivisionError, Exception)
                          ])
def test_subclass(test_object, expected_result):
    """
    verify subclass belongs to class
    """

    assert issubclass(test_object, expected_result)


@pytest.mark.parametrize("test_object",
                         [bool, object, int, float, str, tuple,
                          list, range, set, dict, some_lambda,
                          some_gen_func, some_func
                          ])
def test_callable(test_object):
    """
    verify some objects are callable
    """

    assert callable(test_object)
