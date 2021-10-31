import pytest


@pytest.mark.parametrize("number, result", [
    (-10, 10),
    (-1.15, 1.15),
    (0, 0),
])
def test_abs(number, result):
    """Verify that abs returns modulus of a number"""
    assert abs(number) == result


def test_all():
    """Verify that all() returns True only when all elements are true"""
    x = [1, 2*2, True]
    y = [1, 0, True]
    assert all(x)
    assert not all(y)


def test_any():
    """Verify that any() returns True when at least one element is True"""
    x = [1, 0, True]
    assert any(x)


def test_bool():
    """Basic test for bool() function"""
    assert bool(1 > 0)


def test_callable():
    """basic test for callable()"""
    assert callable(lambda i: print('Hello World'))


def test_dict():
    assert isinstance(dict(), dict)
    assert dict([('x', 5), ('y', -5)]) == {'x': 5, 'y': -5}


def test_dir():
    assert 'split' in dir(str())


@pytest.mark.parametrize("number1, number2, result", [
    (10, 3, (3, 1)),
    (10, 2, (5, 0)),
    (0, 5, (0, 0))
])
def test_div_mod(number1, number2, result):
    assert divmod(number1, number2) == result


def test_enumerate():
    assert list(enumerate(['apple', 'banana'], start=1)) == [(1, 'apple'), (2, 'banana')]
    # todo: add more tests for enumerate
