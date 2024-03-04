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

    @classmethod
    def convert(cls, item):
        if isinstance(item, int):
            return cls(item, 1)
        elif isinstance(item, cls):
            return item

    @classmethod
    def can_be_converted(cls, other):
        return isinstance(other, (cls, int))

    def __repr__(self):
        return f"Fraction({self.num}, {self.denom})"

    def __str__(self):
        return f"\'{self.num} / {self.denom}\'"

    # division
    def __truediv__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        return Fraction(self.num * other.denom, self.denom * other.num)

    def __rtruediv__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        return Fraction(other.num * self.denom, other.denom * self.num)

    # add
    def __add__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        denominator = self.denom * other.denom
        numerator = self.num * other.denom + other.num * self.denom
        return Fraction(numerator, denominator)

    def __radd__(self, other):
        return self.__add__(other)

    # subtraction
    def __sub__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        denominator = self.denom * other.denom
        numerator = self.num * other.denom - other.num * self.denom
        return Fraction(numerator, denominator)

    def __rsub__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        denominator = other.denom * self.denom
        numerator = other.num * self.denom - self.num * other.denom
        return Fraction(numerator, denominator)

    # multiplication
    def __mul__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        denominator = self.denom * other.denom
        numerator = self.num * other.num
        return Fraction(numerator, denominator)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __bool__(self):
        return bool(self.num)

    # >=
    def __ge__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        return self.num * other.denom >= other.num * self.denom

    # >
    def __gt__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        return self.num * other.denom > other.num * self.denom

    # <
    def __lt__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        return self.num * other.denom < other.num * self.denom

    # <=
    def __le__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        return self.num * other.denom <= other.num * self.denom

    def __eq__(self, other):
        if not Fraction.can_be_converted(other):
            return NotImplemented
        other = Fraction.convert(other)
        return self.denom == other.denom and self.num == other.num

    # absolute value
    def __abs__(self):
        return Fraction(abs(self.num), self.denom)

    # negative value
    def __neg__(self):
        return Fraction(self.num * -1, self.denom)
