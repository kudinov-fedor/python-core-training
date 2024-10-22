"""
Create decorator, which will retry inner function multiple times until it passes
"""
import random


def retry(retry_count=5):
    def inner(func):

        def wrapper(*args, **kwargs):
            if retry_count > 0:
                for i in range(0, retry_count):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(e)
                return "Exception"
            else:
                while True:
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(e)

        return wrapper

    return inner


@retry(5)
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
