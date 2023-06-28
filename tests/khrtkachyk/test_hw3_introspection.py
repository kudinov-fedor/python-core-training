import pytest

# 1. Tests for "test_check_ident_equal" function
a = lambda a: a
b = lambda b: b


@pytest.mark.parametrize("a", [
    [1, 2, 3],
    (1, 2, 3),
    ([1, 2], [3, 4]),
    (lambda: ([1, 2], [3, 4]))
])
def test_check_ident_equal(a):
    """
    Create two references to one object
    Check that two references' objects are identical and equal
    """
    b = a
    assert a is b
    assert a == b


# 2. Tests for "test_callable" function
c = lambda c: c


def new_func():
    return c


@pytest.mark.parametrize(["par", "res"], [
    (lambda: True, False),
    (lambda: [1, 2, 3], False),
    (lambda: (bool, int), False),
    (lambda: c, True),
    (lambda: new_func(), True)
])
def test_callable(par, res):
    """
    Check whether a specific parameter is callable
    """
    assert callable(par()) is res


# 3. Tests for "test_identity" function
@pytest.mark.parametrize(["par1", "par2", "res1"], [
    (lambda: ([1, 2], [3, 4]), lambda: ([1, 2], [3, 4]), False)
])
def test_identity(par1, par2, res1):
    """
    Create two lambda-functions with the same expression
    Check that two lambda-functions are not identical
    """
    assert (par1() is par2()) is res1


# 4. Tests for "test_type_class_checks" function
class myClass:
    try:
        5 / 0
    except ZeroDivisionError as error:
        raised_error = error

myclass_instance = myClass()


@pytest.mark.parametrize(["par3", "par4", "res2"], [
    ((lambda: True), bool, False),
    (3.2, float, True),
    ("Hi", (float, str, list, tuple, dict, repr(str)), True),
    ("Hello", (float, list, tuple, dict), False),
    (myclass_instance, myClass, True),
    (myclass_instance, (int, dict, str), False),
    (myClass.raised_error, ZeroDivisionError, True),
])
def test_type_class_checks(par3, par4, res2):
    """
    Check whether an object is of specific class
    """
    assert (isinstance(par3, par4)) is res2
