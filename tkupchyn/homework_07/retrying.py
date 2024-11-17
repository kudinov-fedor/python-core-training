"""
Create decorator, which will retry inner function multiple times untill it passes
"""
from functools import wraps
import random


def retry_till_success(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        while True:
            try:
                return fn(*args, **kwargs)
            except ValueError:
                continue

    return inner


@retry_till_success
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
