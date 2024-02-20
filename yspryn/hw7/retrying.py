"""
Create decorator, which will retry inner function multiple times untill it passes
"""
import random


def retry_function(test_func):
    def wrapper(*args, **kwargs):
        counter = 0
        while True:
            try:
                return test_func(*args, **kwargs)
            except Exception:
                counter += 1
                if counter > 5:
                    raise
    return wrapper


@retry_function
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
