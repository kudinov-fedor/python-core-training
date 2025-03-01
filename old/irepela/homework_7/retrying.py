"""
Create decorator, which will retry inner function multiple times until it passes
"""
import random


def retry(retry_count=-1):

    def inner(func):

        def wrapper(*args, **kwargs):

            nonlocal retry_count

            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
                    retry_count -= 1
                    if retry_count == 0:
                        raise

        return wrapper

    return inner


@retry(5)
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
