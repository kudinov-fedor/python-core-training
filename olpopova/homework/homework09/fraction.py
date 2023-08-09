from math import gcd


class Fraction:

    def __init__(self, num: int, denom: int = 1):

        # convert float to int
        if isinstance(num, float):
            num, _denom = num.as_integer_ratio()
            denom = _denom

        if denom == 0:
            raise ZeroDivisionError

        _gcd = gcd(num, denom)
        self.num = num // _gcd
        self.denom = denom // _gcd

        if self.denom < 0:
            self.num *= -1
            self.denom *= -1

    @staticmethod
    def convert_to_int(item):
        if isinstance(item, (int, float)):
            converted = Fraction(item)
            return converted
        elif isinstance(item, Fraction):
            return item
        return NotImplemented

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
        self, other = self.convert_to_int(self), self.convert_to_int(other)
        return self.num == other.num and self.denom == other.denom

    def __gt__(self, other):
        return self.num * other.denom > other.num * self.denom

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not self > other

    def __le__(self, other):
        return not self > other or self == other

    def __add__(self, other):
        self, other = self.convert_to_int(self), self.convert_to_int(other)
        return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)

    __radd__ = __add__

    def __sub__(self, other):
        self, other = self.convert_to_int(self), self.convert_to_int(other)
        return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)

    def __rsub__(self, other):
        self, other = self.convert_to_int(self), self.convert_to_int(other)
        return other - self

    def __mul__(self, other):
        self, other = self.convert_to_int(self), self.convert_to_int(other)
        num = self.num * other.num
        denom = self.denom * other.denom
        return num // denom if num % denom == 0 else Fraction(num, denom)

    __rmul__ = __mul__

    def __truediv__(self, other):
        self, other = self.convert_to_int(self), self.convert_to_int(other)
        num = self.num * other.denom
        denom = self.denom * other.num
        return num // denom if num % denom == 0 else Fraction(num, denom)

    def __rtruediv__(self, other):
        self, other = self.convert_to_int(self), self.convert_to_int(other)
        return other / self

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __abs__(self):
        return Fraction(abs(self.num), self.denom)
