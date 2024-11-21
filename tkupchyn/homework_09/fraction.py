from math import gcd


class Fraction:

    def __init__(self, nominator: (int, str, float), denominator: int = 1):

        if isinstance(nominator, float):
            nominator = str(nominator)

        if isinstance(nominator, str):
            if '.' in nominator:
                integer_part, fractional_part = nominator.split('.')
                nominator = int(integer_part + fractional_part)
                denominator = 10 ** len(fractional_part)

            elif '/' in nominator:
                nominator, denominator = nominator.split('/')
                nominator = int(nominator)
                denominator = int(denominator)
            elif isinstance(nominator, int):
                pass
            else:
                raise ValueError

        if denominator == 0:
            raise ZeroDivisionError

        _gcd = gcd(nominator, denominator)
        self.num = nominator // _gcd
        self.denom = denominator // _gcd

        if self.denom < 0:
            self.num *= -1
            self.denom *= -1

    def __repr__(self):
        return f'{self.__class__.__name__}({self.num}, {self.denom})'

    def __str__(self):
        return f"'{self.num} / {self.denom}'"

    def __format__(self, format_spec):
        return f'{self.num / self.denom}' if format_spec == 'dec' else self.__str__()
