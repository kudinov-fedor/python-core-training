from math import gcd
from functools import total_ordering


@total_ordering
class Fraction:
    """
     Class that is designed for fractional values numerator/denominator
    """

    def __init__(self, num: int, denom: int = 1):
        """When you call the class constructor without second argument,
        it creates a new fraction representing the number."""

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
        return f"'{self.num}/{self.denom}'"

    def __format__(self, format_spec):
        if format_spec == "dec":
            return str(self.num / self.denom)
        return str(self)

    def __bool__(self):
        return bool(self.num)

    @staticmethod
    def _change_other(other):
        if isinstance(other, int):
            return Fraction(other)
        return other

    def __eq__(self, other):
        if not isinstance(other, (Fraction, int)):
            return NotImplemented

        other = self._change_other(other)

        result = self.num == other.num and self.denom == other.denom

        return result

    def __lt__(self, other):
        if not isinstance(other, (Fraction, int)):
            return NotImplemented

        other = self._change_other(other)

        result = self.num * other.denom < self.denom * other.num

        return result

    def __add__(self, other):
        if not isinstance(other, (Fraction, int)):
            return NotImplemented

        other = self._change_other(other)

        result = Fraction(self.num * other.denom + other.num * self.denom,
                            self.denom * other.denom)

        return result

    __radd__ = __add__
    __iadd__ = __add__

    def __mul__(self, other):
        if not isinstance(other, (Fraction, int)):
            return NotImplemented

        other = self._change_other(other)
        result = Fraction(self.num * other.num, self.denom * other.denom)

        return result

    __rmul__ = __mul__
    __imul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, (Fraction, int)):
            return NotImplemented

        other = self._change_other(other)

        result = Fraction(self.num * other.denom, self.denom * other.num)

        return result

    def __rtruediv__(self, other):
        if not isinstance(other, (Fraction, int)):
            return NotImplemented

        other = self._change_other(other)
        result = other / self

        return result

    __itruediv__ = __truediv__

    def __sub__(self, other):
        return self + (other * (-1))

    def __rsub__(self, other):
        if not isinstance(other, (Fraction, int)):
            return NotImplemented

        other = self._change_other(other)

        result = other - self

        return result

    __isub__ = __sub__

    def __neg__(self):
        return self * (-1)

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)


if __name__ == "__main__":
    a = Fraction(3, -9)
    b = Fraction(0, 1)
    print(a)
    print(bool(b))
    print(1/6 == 2/12)
