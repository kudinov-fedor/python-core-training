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

    @staticmethod
    def convert_to_fraction(number):
        if not isinstance(number, Fraction):
            return Fraction(number)
        else:
            return number

    def __repr__(self):
        return f'{self.__class__.__name__}({self.num}, {self.denom})'

    def __str__(self):
        return f"'{self.num} / {self.denom}'"

    def __format__(self, format_spec):
        return f'{self.num / self.denom}' if format_spec == 'dec' else self.__str__()

    def __bool__(self):
        return bool(self.num)

    def __eq__(self, other):
        other = self.convert_to_fraction(other)
        return self.num == other.num and self.denom == other.denom

    def __lt__(self, other):
        other = self.convert_to_fraction(other)
        return (self.num / self.denom) < (other.num / other.denom)

    def __ge__(self, other):
        other = self.convert_to_fraction(other)
        return (self.num / self.denom) >= (other.num / other.denom)

    def __add__(self, other):
        other = self.convert_to_fraction(other)
        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        return Fraction(num, denom)

    __radd__ = __add__
    __iadd__ = __add__

    def __sub__(self, other):
        other = self.convert_to_fraction(other)
        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __rsub__(self, other):
        other = self.convert_to_fraction(other)
        num = other.num * self.denom - self.num * other.denom
        denom = self.denom * other.denom
        return Fraction(num, denom)

    __isub__ = __sub__

    def __mul__(self, other):
        other = self.convert_to_fraction(other)
        return Fraction(self.num * other.num, self.denom * other.denom)

    __rmul__ = __mul__
    __imul__ = __mul__

    def __truediv__(self, other):
        other = self.convert_to_fraction(other)
        return Fraction(self.num * other.denom, self.denom * other.num)

    def __rtruediv__(self, other):
        other = self.convert_to_fraction(other)
        return other.__truediv__(self)

    __itruediv__ = __truediv__

    def __neg__(self):
        return Fraction(- self.num, self.denom)

    def __abs__(self):
        return Fraction(abs(self.num), abs(self.denom))
