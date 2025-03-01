"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""
from functools import wraps


def caching(fn):
    cache = {}

    @wraps(fn)
    def inner(n):
        nonlocal cache

        if n in cache:
            return cache[n]
        else:
            cache[n] = fn(n)
        return cache[n]

    return inner


def fibo(n: int):
    """
    Count fibonache numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """
    if n < 3:
        return [0, 1, 1][n]
    return fibo(n - 1) + fibo(n - 2)
