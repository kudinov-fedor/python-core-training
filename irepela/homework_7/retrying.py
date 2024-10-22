"""
Create decorator, which will retry inner function multiple times until it passes
"""
import random


def retry(retry_count=5):
    def inner(func):

        def limited_wrapper(*args, **kwargs):
            exception = None
            for i in range(0, retry_count):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    exception = e
                    print(e)
            raise exception

        def unlimited_wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)

        return limited_wrapper if retry_count else unlimited_wrapper

    return inner


@retry(5)
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
