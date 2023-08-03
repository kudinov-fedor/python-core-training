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
        if isinstance(other, Fraction):
            return self.num == other.num and self.denom == other.denom
        return self == other

    def __gt__(self, other):
        return self.num * other.denom > other.num * self.denom

    def __ge__(self, other):
        return self.num * other.denom > other.num * self.denom or self.num == other.num and self.denom == other.denom

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return other - self

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.num
        denom = self.denom * other.denom
        return num // denom if num % denom == 0 else Fraction(num, denom)
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        num = self.num * other.denom
        denom = self.denom * other.num
        return num // denom if num % denom == 0 else Fraction(num, denom)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return other / self

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)
