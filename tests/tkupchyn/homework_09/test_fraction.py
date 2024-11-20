from tkupchyn.homework_09.fraction import Fraction


class Answer:
    def __init__(self, val: str):
        self.val = val

    def __add__(self, other: Fraction):
        return f'{self.val} + {other.num}/{other.denom}'


def test_representation():
    a = Fraction(2, 4)
    assert (a.num, a.denom) == (1, 2)
    z = Fraction(2, -4)

    assert (z.num, z.denom) == (-1, 2)
    assert repr(a) == "Fraction(1, 2)"
    assert str(a) == "'1 / 2'"
    assert "val: {:dec}".format(a) == "val: 0.5"
    assert "val: {}".format(a) == "val: '1 / 2'"


def test_logic_operators():
    # bool assert
    assert Fraction(1, 2)
    assert not Fraction(0)
    # bool operations
    assert Fraction(2, 4) == Fraction(5, 10)
    assert not (Fraction(1, 2) != Fraction(1, 2))
    assert Fraction(1, 2) > Fraction(1, 3)
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)


def test_math_operations():
    # add
    assert Fraction(2, 4) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, 2) + 2 == Fraction(5, 2)
    assert 2 + Fraction(1, 2) == Fraction(5, 2)
    assert Fraction(3, 4) + Answer('4') == '4 + 3/4'

    # in place add
    a = Fraction(2, 4)
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


def test_unary_operations():
    assert -Fraction(1, 2) == Fraction(-1, 2)
    assert abs(Fraction(-1, 2)) == Fraction(1, 2)
