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

    def __repr__(self):
        return f"Fraction({self.num}, {self.denom})"

    def __str__(self):
        return f"\'{self.num} / {self.denom}\'"

    # division
    def __truediv__(self, other):
        value1 = Fraction.convert(self)
        value2 = Fraction.convert(other)
        if (value1.num * value2.denom) % (value1.denom * value2.num) == 0:
            return (value1.num * value2.denom) / (value1.denom * value2.num)
        else:
            return Fraction(value1.num*value2.denom, value1.denom*value2.num)

    def __rtruediv__(self, other):
        value1 = Fraction.convert(other)
        value2 = Fraction.convert(self)
        if (value1.num * value2.denom) % (value1.denom * value2.num) == 0:
            return (value1.num * value2.denom) / (value1.denom * value2.num)
        else:
            return Fraction(value1.num * value2.denom, value1.denom * value2.num)

    # add
    def __add__(self, other):
        value1 = Fraction.convert(self)
        value2 = Fraction.convert(other)
        denominator = value1.denom * value2.denom
        numerator = value1.num * value2.denom + value2.num * value1.denom
        if numerator % denominator == 0:
            return numerator / denominator
        return Fraction(numerator, denominator)

    def __radd__(self, other):
        return self.__add__(other)

    # subtraction
    def __sub__(self, other):
        value1 = Fraction.convert(self)
        value2 = Fraction.convert(other)
        denominator = value1.denom * value2.denom
        numerator = value1.num * value2.denom - value2.num * value1.denom
        if numerator % denominator == 0:
            return numerator / denominator
        return Fraction(numerator, denominator)

    def __rsub__(self, other):
        value1 = Fraction.convert(other)
        value2 = Fraction.convert(self)
        denominator = value1.denom * value2.denom
        numerator = value1.num * value2.denom - value2.num * value1.denom
        if numerator % denominator == 0:
            return numerator / denominator
        return Fraction(numerator, denominator)

    # multiplication
    def __mul__(self, other):
        value1 = Fraction.convert(self)
        value2 = Fraction.convert(other)
        denominator = value1.denom * value2.denom
        numerator = value1.num * value2.num
        if numerator % denominator == 0:
            return numerator / denominator
        return Fraction(numerator, denominator)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __bool__(self):
        if self.denom and self.num:
            return True
        else:
            return False

    # >=
    def __ge__(self, other):
        return self.num/self.denom >= other.num/other.denom

    # >
    def __gt__(self, other):
        return self.num / self.denom > other.num / other.denom

    # <
    def __lt__(self, other):
        return self.num / self.denom < other.num / other.denom

    # <=
    def __le__(self, other):
        return self.num / self.denom <= other.num / other.denom

    def __eq__(self, other):
        if self.denom == other.denom and self.num == other.num:
            return True
        else:
            return False

    # absolute value
    def __abs__(self):
        if self.denom < 0:
            self.denom *= -1
        elif self.num < 0:
            self.num *= -1
        return Fraction(self.num, self.denom)

    # negative value
    def __neg__(self):
        return Fraction(self.num * -1, self.denom)
