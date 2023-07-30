from math import gcd


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
        return f"Fraction({self.num}, {self.denom})"

    def __str__(self):
        return f"'{self.num} / {self.denom}'"

    def __format__(self, format_spec):
        if format_spec == "dec":
            return "{:.1f}".format(self.num/self.denom)
        else:
            return "'{} / {}'".format(self.num, self.denom)

    def __bool__(self):
        return self.num != 0

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.num, self.denom) == (other.num, other.denom)
        elif isinstance(other, int):
            return self.num == other and self.denom == 1
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Fraction):
            return (self.num, self.denom) != (other.num, other.denom)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return (self.num / self.denom) > (other.num / other.denom)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return (self.num / self.denom) < (other.num / other.denom)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return (self.num / self.denom) >= (other.num / other.denom)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fraction):
            return (self.num / self.denom) <= (other.num / other.denom)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom + other.num * self.denom
            new_denom = self.denom * other.denom
            return Fraction(new_num, new_denom)
        elif isinstance(other, int):
            return self + Fraction(other)

        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return Fraction(other) + self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom - other.num * self.denom
            new_denom = self.denom * other.denom
            return Fraction(new_num, new_denom)
        elif isinstance(other, int):
            return self - Fraction(other)

        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return Fraction(other) - self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.num
            new_denom = self.denom * other.denom
            return Fraction(new_num, new_denom)
        elif isinstance(other, int):
            return Fraction(self.num * other, self.denom)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom
            new_denom = self.denom * other.num
            return Fraction(new_num, new_denom)
        elif isinstance(other, int):
            return Fraction(self.num, self.denom * other)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.denom, self.num)
        return NotImplemented


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

    # in place sub
    b = a
    b -= 2
    assert b is not a
    assert b == Fraction(-3, 2)

    assert Fraction(1, 3) * 3 == 1
    assert Fraction(2, 3) * Fraction(12, 4) == 2
    assert 2 * Fraction(3, 2) == 3

    # div
    assert Fraction(2, 3) / Fraction(2, 3) == 1
    assert Fraction(2, 3) / Fraction(4, 3) == Fraction(1, 2)
    assert 2 / Fraction(4, 3) == Fraction(3, 2)
