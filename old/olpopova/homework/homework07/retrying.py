"""
Create decorator, which will retry inner function multiple times until it passes
"""


import random


def retry_decorator(function):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return function(*args, **kwargs)
            except Exception as e:
                print(e)
                continue

    return wrapper


@retry_decorator
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def test_retry_func():
    print(unstable_function())
