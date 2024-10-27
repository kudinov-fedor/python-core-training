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
        return f"Fraction({self.num}, {self.denom})"

    def __str__(self):
        return f"'{self.num} / {self.denom}'"

    def __format__(self, fmt):
        if fmt == "dec":
            return str(self.num / self.denom)
        return str(self)

    def __bool__(self):
        return bool(self.num)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num == other.num and self.denom == other.denom
        elif isinstance(other, int):
            return self == Fraction(other)
        else:
            raise NotImplementedError

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom < self.denom * other.num
        else:
            raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom + other.num * self.denom,
                            self.denom * other.denom)
        elif isinstance(other, int):
            return self + Fraction(other)
        else:
            raise NotImplementedError

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom - other.num * self.denom,
                            self.denom * other.denom)
        elif isinstance(other, int):
            return self - Fraction(other)
        else:
            raise NotImplementedError

    def __rsub__(self, other):
        return Fraction(other) - self

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.num, self.denom * other.denom)
        elif isinstance(other, int):
            return self * Fraction(other)
        else:
            raise NotImplementedError

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.num * other.denom, self.denom * other.num)
        elif isinstance(other, int):
            return self / Fraction(other)
        else:
            raise NotImplementedError

    def __rtruediv__(self, other):
        return Fraction(other) / self

    def __neg__(self):
        return -1 * self

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)
