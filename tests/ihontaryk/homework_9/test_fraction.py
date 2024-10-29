from audioop import add, mul
from operator import lt, le, eq, ne, ge, gt

import pytest

from ihontaryk.homework_9.fraction import Fraction


@pytest.mark.parametrize('num, denom, expected_result',
                         [(1, 2, "Fraction(1, 2)"),
                          ])
def test_repr(num, denom, expected_result):
    """
    verify repr function
    """
    a = Fraction(num, denom)
    assert repr(a) == expected_result


@pytest.mark.parametrize('num, denom, expected_result',
                         [(1, 2, "'1/2'"),
                          (5, -25, "'-1/5'"),
                          ])
def test_str(num, denom, expected_result):
    """
    verify str function
    """
    a = Fraction(num, denom)
    assert str(a) == expected_result


@pytest.mark.parametrize('num, denom, expected_result',
                         [(1, 2, "0.5"),
                          (2, 2, "1.0"),
                          ])
def test_dec(num, denom, expected_result):
    """
    verify dec function
    """
    a = Fraction(num, denom)
    assert "{:dec}".format(a) == expected_result


@pytest.mark.parametrize('num1, denom1, num2, denom2, func, expected_result',
                         [(1, 2, 2, 5, lt, False),
                          (2, 4, 3, 6, le, True),
                          (-2, 4, 3, -6, eq, True),
                          (1, 4, 3, 5, ne, True),
                          (1, -4, -2, 8, ge, True),
                          (1, 4, 2, 8, gt, False),
                          ])
def test_logic_operators(num1, denom1, num2, denom2, func, expected_result):
    """
    verify logic operators
    """
    a = Fraction(num1, denom1)
    b = Fraction(num2, denom2)
    assert func(a, b) is expected_result


@pytest.mark.parametrize('num1, denom1, num2, denom2, func, expected_result',
                         [(1, 2, 2, 5, Fraction.__add__, "'9/10'"),
                          (2, 5, 3, 7, Fraction.__sub__, "'-1/35'"),
                          (-2, 4, 3, -6, Fraction.__mul__, "'1/4'"),
                          (3, 4, 3, 5, Fraction.__truediv__, "'5/4'"),
                          ])
def test_arithmetic_operators(num1, denom1, num2, denom2, func, expected_result):
    """
    verify arithmetic operators
    """
    a = Fraction(num1, denom1)
    b = Fraction(num2, denom2)

    assert str(func(a, b)) == expected_result


@pytest.mark.parametrize('num, denom, expected_result',
                         [(-1, 2, "'1/2'"),
                          (2, -3, "'2/3'"),
                          ])
def test_abs(num, denom, expected_result):
    """
    verify abs function
    """
    a = Fraction(num, denom)
    assert str(abs(a)) == expected_result
