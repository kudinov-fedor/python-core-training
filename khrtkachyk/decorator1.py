import pytest
"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""


def my_decor(original_func):
    cached = {}

    def wrapper(n: int):
        if n in cached:
            return original_func
        elif n not in cached:
            res = original_func(n)
            return res
    return wrapper


@my_decor
def fibo(n: int):
    """
    Count fibonache numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """
    if n < 3:
        return [0, 1, 2][n]
    return fibo(n - 1) + fibo(n - 2)


def test_decorator(given_range, res):
    ints = []
    for i in range(given_range):
        ints.append(fibo(i))
    assert ints == res


parametrized_decor = pytest.mark.parametrize("given_range, res", [
    (10, [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
    (1, [0]),
    (3, [0, 1, 2]),
    (12, [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]),
    (0, [])
])

test_decorator = parametrized_decor(test_decorator)
