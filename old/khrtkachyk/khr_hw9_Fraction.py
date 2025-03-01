from math import gcd


class Fraction:

    def __init__(self, num: int, denom: int = 1):

        # convert to fraction
        if isinstance(num, float):
            num, _denom = num.as_integer_ratio()
            denom = denom * _denom
        elif isinstance(num, type(self)):
            num, _denom = num.num, num.denom
            denom = _denom * denom

        if denom == 0:
            raise ZeroDivisionError

        _gcd = gcd(num, denom)
        self.num = num // _gcd
        self.denom = denom // _gcd

        if self.denom < 0:
            self.num *= -1
            self.denom *= -1

    def __repr__(self):
        return f'Fraction({self.num}, {self.denom})'

    def __str__(self):
        return f"'{self.num} / {self.denom}'"

    def __format__(self, format_spec):
        if format_spec == "dec":
            return str(f'{float(self.num) / float(self.denom)}')
        return str(self)

    def __bool__(self):
        return bool(self.num)

    @classmethod
    def can_convert(cls, item) -> bool:
        return isinstance(item, (int, float, cls))

    def __eq__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        return str(self) == str(other)

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        return self.num * other.denom > other.num * self.denom

    def __ge__(self, other):
        return self == other or self > other

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return self == other or self < other

    def __add__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        num = (self.num * other.denom) + (other.num * self.denom)
        return Fraction(num, (self.denom * other.denom))

    __radd__ = __add__

    def __sub__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        num = (self.num * other.denom) - (other.num * self.denom)
        return Fraction(num, (self.denom * other.denom))

    def __rsub__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        return other - self

    def __mul__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        return Fraction(self.num * other.num, self.denom * other.denom)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        return Fraction(self.num * other.denom, self.denom * other.num)

    def __rtruediv__(self, other):
        if not self.can_convert(other):
            return NotImplemented

        other = Fraction(other)
        return other / self

    def __neg__(self):
        return Fraction(-self.num, self.denom)

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
    assert Fraction(1, 2) == 0.5
    assert Fraction(4, 2) == 2
    assert Fraction(4, 2) != 3
    assert Fraction(1, 2) != 0.6
    assert Fraction(3, 4) != Fraction(5, 6)
    assert not (Fraction(1, 2) != Fraction(1, 2))
    assert Fraction(1, 2) > Fraction(1, 3)
    assert Fraction(1, 2) > -1
    assert Fraction(1, 2) > 0.1
    assert Fraction(1, 3) < Fraction(1, 2)
    assert Fraction(1, 3) < 2
    assert Fraction(1, 3) < 0.9
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 3) <= 2
    assert Fraction(1, 3) <= 0.9
    assert Fraction(1, 2) <= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(1, 3)
    assert Fraction(1, 2) >= -1
    assert Fraction(1, 2) >= 0.5

    # add
    assert Fraction(2, 4) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, 2) + 2 == Fraction(5, 2)
    assert 2 + Fraction(1, 2) == Fraction(5, 2)
    assert Fraction(1, 2) + 0.5 == Fraction(2, 2)
    assert 0.5 + Fraction(1, 2) == Fraction(2, 2)
    assert 2 + Fraction(1, 2) == Fraction(5, 2)
    assert Fraction(2, 4) + Fraction(1, 4) == Fraction(3, 4)
    try:
        assert "123" + Fraction(123, 1) == Fraction(246, 1)
        assert Fraction(1, 2) + "abc" == "0.5 + abc"
    except TypeError as e:
        assert "unsupported operand" or "concatenate" in str(e)
        ...
    else:
        raise AssertionError

    # in place add
    b = a
    b += 2
    assert b is not a
    assert b == Fraction(5, 2)

    # sub
    assert Fraction(2, 4) - Fraction(1, 3) == Fraction(1, 6)
    assert Fraction(5, 2) - 2 == Fraction(1, 2)
    assert Fraction(5, 2) - 0.5 == Fraction(4, 2)
    assert 2 - Fraction(5, 2) == Fraction(-1, 2)
    assert 0.5 - Fraction(5, 2) == Fraction(-4, 2)

    # in place sub
    b = a
    b -= 2
    assert b is not a
    assert b == Fraction(-3, 2)

    # mul
    assert Fraction(1, 3) * 3 == 1
    assert Fraction(2, 3) * Fraction(12, 4) == 2
    assert 2 * Fraction(3, 2) == 3
    assert Fraction(1, 3) * 0.5 == Fraction(1, 6)

    # in place mul
    b = a
    b *= 2
    assert b is not a
    assert b == 1

    # div
    assert Fraction(2, 3) / Fraction(2, 3) == 1
    assert Fraction(2, 3) / Fraction(4, 3) == Fraction(1, 2)
    assert 2 / Fraction(4, 3) == Fraction(3, 2)
    assert 0.5 / Fraction(2, 3) == Fraction(3, 4)
    assert Fraction(5, 2) / 0.5 == Fraction(5, 1)

    # in place div
    b = a
    b /= 2
    assert b is not a
    assert b == Fraction(1, 4)

    # negation
    assert -Fraction(1, 2) == Fraction(-1, 2)

    # absolute value
    assert abs(Fraction(-1, 2)) == Fraction(1, 2)

    # converting to fraction
    assert Fraction.can_convert(123)
    assert Fraction.can_convert(5.6)
    assert Fraction.can_convert(Fraction(1, 2))

    assert Fraction(1).can_convert(123)
    assert Fraction(1).can_convert(5.6)
    assert Fraction(1).can_convert(Fraction(1, 2))

    assert Fraction(0.5) == Fraction(1, 2)
    assert Fraction(0.5, 2) == Fraction(1, 4)
    assert Fraction(Fraction(1, 2)) == Fraction(1, 2)
    assert Fraction(Fraction(1, 2), 2) == Fraction(1, 4)

    assert 134 - Fraction(134, 1) == 0
    try:
        assert "134" - Fraction(134, 1) == 0
    except TypeError as e:
        assert str(e) == "unsupported operand type(s) for -: 'str' and 'Fraction'"
        ...
    else:
        raise AssertionError

    assert Fraction(9, 2) / Fraction(2) == 9/4

