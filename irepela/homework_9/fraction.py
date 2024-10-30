from math import gcd
from functools import total_ordering


@total_ordering
class Fraction:

    def __init__(self, num, denom: int = 1):

        if denom == 0:
            raise ZeroDivisionError

        input_num = num
        input_denom = denom

        if isinstance(num, Fraction):
            input_num = num.num
            input_denom = num.denom

        _gcd = gcd(input_num, input_denom)
        self.num = input_num // _gcd
        self.denom = input_denom // _gcd

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

    @staticmethod
    def can_convert(other):
        return isinstance(other, (Fraction, int))

    def __eq__(self, other):
        if not self.can_convert(other):         # check if need to proceed
            return NotImplemented
        other = Fraction(other)
        result = self.num == other.num and self.denom == other.denom
        return result

    def __lt__(self, other):
        if not self.can_convert(other):  # check if need to proceed
            return NotImplemented
        other = Fraction(other)
        result = self.num * other.denom < self.denom * other.num
        return result

    def __add__(self, other):
        if not self.can_convert(other):  # check if need to proceed
            return NotImplemented
        other = Fraction(other)
        result = Fraction(self.num * other.denom + other.num * self.denom,
                          self.denom * other.denom)
        return result

    __radd__ = __add__

    def __sub__(self, other):
        if not self.can_convert(other):  # check if need to proceed
            return NotImplemented
        other = Fraction(other)
        result = Fraction(self.num * other.denom - other.num * self.denom,
                          self.denom * other.denom)
        return result

    def __rsub__(self, other):
        return Fraction(other) - self

    def __mul__(self, other):
        if not self.can_convert(other):  # check if need to proceed
            return NotImplemented
        other = Fraction(other)
        result = Fraction(self.num * other.num, self.denom * other.denom)
        return result

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not self.can_convert(other):  # check if need to proceed
            return NotImplemented
        other = Fraction(other)
        result = Fraction(self.num * other.denom, self.denom * other.num)
        return result

    def __rtruediv__(self, other):
        return Fraction(other) / self

    def __neg__(self):
        return -1 * self

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)
