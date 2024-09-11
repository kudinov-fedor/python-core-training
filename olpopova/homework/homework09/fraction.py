from math import gcd


class Fraction:

    def __init__(self, num: int, denom: int = 1):

        # handle object types

        if isinstance(num, float):
            num, _denom = num.as_integer_ratio()
            denom = _denom
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

    @classmethod
    def conversion_check(cls, item) -> bool:
        return isinstance(item, (int, float, cls))

    def __repr__(self):
        return f'{Fraction.__name__}{self.num, self.denom}'

    def __str__(self):
        return f'\'{self.num} / {self.denom}\''

    def __format__(self, *args):
        if 'dec' in args:
            return f'{self.num / self.denom}'
        return str(self)

    def __bool__(self):
        return self.num != 0

    def __eq__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return self.num == other.num and self.denom == other.denom

    def __gt__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return self.num * other.denom > other.num * self.denom

    def __ge__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return self == other or self > other

    def __lt__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return not self > other

    def __le__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return self == other or not self >= other

    def __add__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    __radd__ = __add__

    def __sub__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def __rsub__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return other - self

    def __mul__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        num = self.num * other.num
        denom = self.denom * other.denom
        return Fraction(num, denom)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        num = self.num * other.denom
        denom = self.denom * other.num
        return Fraction(num, denom)

    def __rtruediv__(self, other):
        if not self.conversion_check(other):
            return NotImplemented

        other = type(self)(other)
        return other / self

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)
