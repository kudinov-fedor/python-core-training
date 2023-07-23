"""
Create decorator, which will retry inner function multiple times until it passes
"""


import random


def retry_decorator(function):
    def wrapper():
        res = None
        while res is None:
            try:
                res = function()
            except ValueError as e:
                print(e)
        return res
    return wrapper


@retry_decorator
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def test_retry_func():
    unstable_function()
