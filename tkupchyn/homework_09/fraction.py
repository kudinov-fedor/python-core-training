from math import gcd


class Fraction:

    def __init__(self, num: (int, str, float), denom: int = 1):

        if isinstance(num, float):
            num = str(num)

        if isinstance(num, str):
            if '.' in num:
                integer_part, fractional_part = num.split('.')
                num = int(integer_part + fractional_part)
                denom = 10 ** len(fractional_part)

            elif '/' in num:
                num, denom = num.split('/')
                num = int(num)
                denom = int(denom)
            elif isinstance(num, int):
                pass
            else:
                raise ValueError

        if denom == 0:
            raise ZeroDivisionError

        _gcd = gcd(num, denom)
        self.num = num // _gcd
        self.denom = denom // _gcd

        if self.denom < 0:
            self.num *= -1
            self.denom *= -1

    def __repr__(self):
        return f'{self.__class__.__name__}({self.num}, {self.denom})'

    def __str__(self):
        return f"'{self.num} / {self.denom}'"

    def __format__(self, format_spec):
        return f'{self.num / self.denom}' if format_spec == 'dec' else self.__str__()
