"""
Create decorator, which will retry inner function multiple times until it passes
"""


import random


def retry(func):

    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)

    return wrapper


@retry
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
