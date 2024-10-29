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

    def convert_to_fraction(self, other):
        result = None
        if isinstance(other, Fraction):
            result = other
        if isinstance(other, int):
            result = Fraction(other)
        return result

    def __eq__(self, other):
        result = NotImplemented
        other_fraction = self.convert_to_fraction(other)
        if other_fraction:
            result = self.num == other_fraction.num and self.denom == other_fraction.denom
        return result

    def __lt__(self, other):
        result = NotImplemented
        other_fraction = self.convert_to_fraction(other)
        if other_fraction:
            result = self.num * other_fraction.denom < self.denom * other_fraction.num
        return result

    def __add__(self, other):
        result = NotImplemented
        other_fraction = self.convert_to_fraction(other)
        if other_fraction:
            result = Fraction(self.num * other_fraction.denom + other_fraction.num * self.denom,
                              self.denom * other_fraction.denom)
        return result

    __radd__ = __add__

    def __sub__(self, other):
        result = NotImplemented
        other_fraction = self.convert_to_fraction(other)
        if other_fraction:
            result = Fraction(self.num * other_fraction.denom - other_fraction.num * self.denom,
                              self.denom * other_fraction.denom)
        return result

    def __rsub__(self, other):
        return Fraction(other) - self

    def __mul__(self, other):
        result = NotImplemented
        other_fraction = self.convert_to_fraction(other)
        if other_fraction:
            result = Fraction(self.num * other_fraction.num, self.denom * other_fraction.denom)
        return result

    __rmul__ = __mul__

    def __truediv__(self, other):
        result = NotImplemented
        other_fraction = self.convert_to_fraction(other)
        if other_fraction:
            result = Fraction(self.num * other_fraction.denom, self.denom * other_fraction.num)
        return result

    def __rtruediv__(self, other):
        return Fraction(other) / self

    def __neg__(self):
        return -1 * self

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)
