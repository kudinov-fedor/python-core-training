from yspryn.hw9.fraction import Fraction
import pytest


def test_fractions():
    a = Fraction(2, 4)
    assert (a.num, a.denom) == (1, 2)

    z = Fraction(2, -4)
    assert (z.num, z.denom) == (-1, 2)

    # str repr
    assert repr(a) == "Fraction(1, 2)"
    assert str(a) == "'1 / 2'"
    # assert "val: {:dec}".format(a) == "val: 0.5"
    # assert "val: {}".format(a) == "val: '1 / 2'"
    #
    # # bool assert
    assert Fraction(1, 2)
    assert not Fraction(0)
    #
    # # logic operators
    assert Fraction(2, 4) == Fraction(5, 10)
    assert not (Fraction(1, 2) != Fraction(1, 2))
    assert Fraction(1, 2) > Fraction(1, 3)
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)
    #
    # # add
    assert Fraction(2, 4) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, 2) + 2 == Fraction(5, 2)
    assert Fraction(1, 2) + Fraction(1, 2) == 1
    #
    # # in place add
    b = a
    b += 2
    assert b is not a
    assert b == Fraction(5, 2)
    #
    # # sub
    assert Fraction(2, 4) - Fraction(1, 3) == Fraction(1, 6)
    assert Fraction(5, 2) - 2 == Fraction(1, 2)
    assert 2 - Fraction(3, 2) == Fraction(1, 2)
    #
    # # in place sub
    b = a
    b -= 2
    assert b is not a
    assert b == Fraction(-3, 2)
    # #
    # # # mul
    assert Fraction(1, 3) * 3 == 1
    assert Fraction(2, 3) * Fraction(12, 4) == 2
    assert 2 * Fraction(3, 2) == 3
    #
    # # in place mul
    b = a
    b *= 2
    assert b is not a
    assert b == 1
    # #
    # # # div
    assert Fraction(2, 3) / Fraction(2, 3) == 1
    assert Fraction(2, 3) / Fraction(4, 3) == Fraction(1, 2)
    assert 2 / Fraction(4, 3) == Fraction(3, 2)
    # #
    # # in place div
    b = a
    b /= 2
    assert b is not a
    assert b == Fraction(1, 4)
    # #
    assert -Fraction(1, 2) == Fraction(-1, 2)
    assert abs(Fraction(-1, 2)) == Fraction(1, 2)

    # not implemented
    assert Fraction(1, 2).__add__("abc") is NotImplemented
    assert Fraction(2, 4).__sub__('test') is NotImplemented
    assert Fraction(2, 4).__mul__('test') is NotImplemented
    assert Fraction(2, 4).__truediv__('test') is NotImplemented
    assert Fraction(1, 2).__eq__("abc") is NotImplemented
    assert Fraction(1, 2).__le__("abc") is NotImplemented
    assert Fraction(1, 2).__lt__("abc") is NotImplemented
    assert Fraction(1, 2).__gt__("abc") is NotImplemented


def test_add_notimplemented():
    with pytest.raises(TypeError):
        Fraction(1, 2) + "abc"
