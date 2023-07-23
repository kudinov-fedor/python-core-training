"""
Create decorator, which will retry inner function multiple times until it passes
"""


import random


def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def retry_func():
    res = None
    while res is None:
        try:
            res = unstable_function()
            return res
        except ValueError as e:
            print(e)


def test_retry_func():
    retry_func()
