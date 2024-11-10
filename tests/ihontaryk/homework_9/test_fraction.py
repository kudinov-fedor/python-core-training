import pytest

from ihontaryk.homework_9.fraction import Fraction


@pytest.mark.parametrize('num, denom, expected_result',
                         [(1, 2, "Fraction(1, 2)"),
                          (1, -1, "Fraction(-1, 1)"),
                          (0, 1, "Fraction(0, 1)")])
def test_repr(num, denom, expected_result):
    """
    verify repr function
    """
    a = Fraction(num, denom)

    assert repr(a) == expected_result


@pytest.mark.parametrize('num, denom, expected_result',
                         [(1, 2, "'1/2'"),
                          (5, -25, "'-1/5'")
                          ])
def test_str(num, denom, expected_result):
    """
    verify str function
    """
    a = Fraction(num, denom)

    assert str(a) == expected_result


@pytest.mark.parametrize('num, denom, expected_result',
                         [(1, 2, "0.5"),
                          (2, 2, "1.0")
                          ])
def test_dec(num, denom, expected_result):
    """
    verify dec function
    """
    a = Fraction(num, denom)

    assert "{:dec}".format(a) == expected_result


@pytest.mark.parametrize('num1, denom1, num2, denom2, func, expected_result',
                         [(1, 2, 2, 5, Fraction.__lt__, False),
                          (2, 4, 3, 6, Fraction.__le__, True),
                          (-2, 4, 3, -6, Fraction.__eq__, True),
                          (-2, 4, 3, -3, Fraction.__eq__, False),
                          (1, 4, 3, 5, Fraction.__ne__, True),
                          (1, -4, -2, 8, Fraction.__ge__, True),
                          (1, 4, 2, 8, Fraction.__gt__, False)
                          ])
def test_logic_operators(num1, denom1, num2, denom2, func, expected_result):
    """
    verify logic operators
    """
    a = Fraction(num1, denom1)
    b = Fraction(num2, denom2)

    assert func(a, b) is expected_result


@pytest.mark.parametrize('num1, denom1, b, func, expected_result',
                         [(1, 2, '2', Fraction.__lt__, NotImplemented),
                          (2, 4, '3', Fraction.__le__, NotImplemented),
                          (-2, 4, '3', Fraction.__eq__, NotImplemented),
                          (-2, 4, '3', Fraction.__eq__, NotImplemented),
                          (1, 4, '3', Fraction.__ne__, NotImplemented),
                          (1, -4, '-2', Fraction.__ge__, NotImplemented),
                          (1, 4, '2', Fraction.__gt__, NotImplemented)
                          ])
def test_not_implemented(num1, denom1, b, func, expected_result):
    """
    verify not_implemented types
    """
    a = Fraction(num1, denom1)

    assert func(a, b) is expected_result


@pytest.mark.parametrize('num1, denom1, b, func, expected_result',
                         [(1, 2, 5, Fraction.__lt__, True),
                          (2, 4, 5, Fraction.__le__, True),
                          (-2, 4, 5, Fraction.__eq__, False),
                          (-4, 2, -2, Fraction.__eq__, True),
                          (1, 4, 5, Fraction.__ne__, True),
                          (1, -4, 5, Fraction.__ge__, False),
                          (1, 4, 5, Fraction.__gt__, False)
                          ])
def test_int_logic(num1, denom1, b, func, expected_result):
    """
    verify int type for second number
    """
    a = Fraction(num1, denom1)

    assert func(a, b) is expected_result


@pytest.mark.parametrize('num1, denom1, num2, denom2, func, expected_result',
                         [(1, 2, 2, 5, Fraction.__add__, "'9/10'"),
                          (2, 5, 3, 7, Fraction.__sub__, "'-1/35'"),
                          (2, 5, 3, 7, Fraction.__rsub__, "'1/35'"),
                          (-2, 4, 3, -6, Fraction.__mul__, "'1/4'"),
                          (3, 4, 3, 5, Fraction.__truediv__, "'5/4'"),
                          (3, 4, 3, 5, Fraction.__rtruediv__, "'4/5'")
                          ])
def test_arithmetic_operators(num1, denom1, num2, denom2, func, expected_result):
    """
    verify arithmetic operators
    """
    a = Fraction(num1, denom1)
    b = Fraction(num2, denom2)

    assert str(func(a, b)) == expected_result


@pytest.mark.parametrize('num1, denom1, b, func, expected_result',
                         [(1, 2, 5, Fraction.__add__, "'11/2'"),
                          (2, 4, 5, Fraction.__sub__, "'-9/2'"),
                          (2, 4, 5, Fraction.__rsub__, "'9/2'"),
                          (-2, 4, 5, Fraction.__mul__, "'-5/2'"),
                          (-4, 2, -2, Fraction.__truediv__, "'1/1'"),
                          (-8, 2, -2, Fraction.__rtruediv__, "'1/2'")
                          ])
def test_int_arithmetic(num1, denom1, b, func, expected_result):
    """
    verify int type for second number
    """
    a = Fraction(num1, denom1)

    assert str(func(a, b)) == expected_result


@pytest.mark.parametrize('num, denom, expected_result',
                         [(-1, 2, "'1/2'"),
                          (2, -3, "'2/3'")
                          ])
def test_abs(num, denom, expected_result):
    """
    verify abs function
    """
    a = Fraction(num, denom)

    assert str(abs(a)) == expected_result
