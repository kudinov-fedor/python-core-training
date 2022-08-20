from math import gcd
from functools import total_ordering


@total_ordering
class Fraction:

    def __init__(self, num: int, denom: int = 1):

        if denom == 0:
            raise ZeroDivisionError

        _gcd = gcd(num, denom)
        self.num = num // _gcd
        self.denom = denom // _gcd

        if self.denom < 0:
            self.num *= -1
            self.denom *= -1

    def __repr__(self):
        return "Fraction({}, {})".format(self.num, self.denom)

    def __str__(self):
        return "'{} / {}'".format(self.num, self.denom)

    def __format__(self, format_spec):
        if format_spec == "dec":
            return str(self.num / self.denom)
        return str(self)

    def __bool__(self):
        return bool(self.num)

    # operators
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num == other.num and self.denom == other.denom
        elif isinstance(other, int):
            return self == Fraction(other)

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom < self.denom * other.num
        elif isinstance(other, int):
            return self < Fraction(other)

        return NotImplemented

    # add
    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom + other.num * self.denom,
                            self.denom * other.denom)
        elif isinstance(other, int):
            return self + Fraction(other)

        return NotImplemented

    __radd__ = __add__
    __iadd__ = __add__

    # mul
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.denom * other.denom)
        elif isinstance(other, int):
            return self * Fraction(other)

        return NotImplemented

    __rmul__ = __mul__
    __imul__ = __mul__

    # div
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom, self.denom * other.num)
        elif isinstance(other, int):
            return self / Fraction(other)

    def __rtruediv__(self, other):
        return Fraction(other) / self

    __itruediv__ = __truediv__

    # sub
    def __sub__(self, other):
        return self + (other * (-1))

    def __rsub__(self, other):
        return Fraction(other) - self

    __isub__ = __sub__

    # unary
    def __neg__(self):
        return self * (-1)

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)


if __name__ == "__main__":

    a = Fraction(2, 4)
    assert (a.num, a.denom) == (1, 2)

    z = Fraction(2, -4)
    assert (z.num, z.denom) == (-1, 2)

    # str repr
    assert repr(a) == "Fraction(1, 2)"
    assert str(a) == "'1 / 2'"
    assert "val: {:dec}".format(a) == "val: 0.5"
    assert "val: {}".format(a) == "val: '1 / 2'"

    # bool assert
    assert Fraction(1, 2)
    assert not Fraction(0)

    # logic operators
    assert Fraction(2, 4) == Fraction(5, 10)
    assert not (Fraction(1, 2) != Fraction(1, 2))
    assert Fraction(1, 2) > Fraction(1, 3)
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)

    # add
    assert Fraction(2, 4) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, 2) + 2 == Fraction(5, 2)
    assert 2 + Fraction(1, 2) == Fraction(5, 2)

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

    assert -Fraction(1, 2) == Fraction(-1, 2)
    assert abs(Fraction(-1, 2)) == Fraction(1, 2)
