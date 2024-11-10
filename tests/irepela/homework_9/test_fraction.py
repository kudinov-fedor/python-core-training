import pytest
from irepela.homework_9.fraction import Fraction


class Custom:

    custom_prop = '5'

    def __radd__(self, other: Fraction) -> str:
        return f'{self.custom_prop} + {other.num}/{other.denom}'


def test_fraction_str():
    a = Fraction(2, 4)
    assert (a.num, a.denom) == (1, 2)

    z = Fraction(2, -4)
    assert (z.num, z.denom) == (-1, 2)

    # str repr
    assert repr(a) == "Fraction(1, 2)"
    assert str(a) == "'1 / 2'"

    # format
    assert "val: {:dec}".format(a) == "val: 0.5"
    assert "val: {}".format(a) == "val: '1 / 2'"


def test_fraction_logic_operators():
    # bool assert
    assert Fraction(1, 2)
    assert not Fraction(0)

    # logic operators
    assert Fraction(2, 4) == Fraction(5, 10)
    assert Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(0, 5) == Fraction(0, 1)
    assert (Fraction(1, 2) != Fraction(1, 2)) is False
    assert Fraction(1, 2) > Fraction(1, 3)
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)


def test_fraction_math_operators():
    a = Fraction(2, 4)

    # add
    assert Fraction(2, 4) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, 2) + 2 == Fraction(5, 2)
    assert 2 + Fraction(1, 2) == Fraction(5, 2)
    assert (Fraction(1, 2) + Custom()) == '5 + 1/2'

    # not valid add
    with pytest.raises(TypeError):
        Fraction(1, 2) + "2"
    with pytest.raises(TypeError):
        "35" + Fraction(1, 2)

    # in place add
    b = a
    b += 2
    assert b is not a
    assert b == Fraction(5, 2)

    # sub
    assert Fraction(2, 4) - Fraction(1, 3) == Fraction(1, 6)
    assert Fraction(5, 2) - 2 == Fraction(1, 2)
    assert 2 - Fraction(3, 2) == Fraction(1, 2)

    # in place sub
    b = a
    b -= 2
    assert b is not a
    assert b == Fraction(-3, 2)

    # mul
    assert Fraction(1, 3) * 3 == 1
    assert Fraction(2, 3) * Fraction(12, 4) == 2
    assert 2 * Fraction(3, 2) == 3

    # in place mul
    b = a
    b *= 2
    assert b is not a
    assert b == 1

    # div
    assert Fraction(2, 3) / Fraction(2, 3) == 1
    assert Fraction(2, 3) / Fraction(4, 3) == Fraction(1, 2)
    assert 2 / Fraction(4, 3) == Fraction(3, 2)

    # in place div
    b = a
    b /= 2
    assert b is not a
    assert b == Fraction(1, 4)


def test_fraction_abs():
    assert -Fraction(1, 2) == Fraction(-1, 2)
    assert abs(Fraction(-1, 2)) == Fraction(1, 2)
