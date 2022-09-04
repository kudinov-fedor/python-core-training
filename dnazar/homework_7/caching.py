"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""


def fibo_without_rec(n: int):
    """
    Count fibonacci numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """

    first, second = 1, 2
    if n < 3:
        return [0, first, second][n]
    else:
        for _ in range(3, n+1):
            first, second = second, first + second
        return second


def fibo_dec(func):
    fibo_cash = {}

    def wrapper(n):
        if n not in fibo_cash:
            fibo_cash[n] = func(n)
        return fibo_cash[n]
    return wrapper


@fibo_dec
def fibo(n: int):
    """
    Count fibonacci numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """
    if n < 3:
        return [0, 1, 2][n]
    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(fibo(i))
