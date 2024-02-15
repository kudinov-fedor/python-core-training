"""
Create decorator, which will retry inner function multiple times untill it passes
"""
import random


def retry_decorator(retries: int = 5, exception_types: tuple = (Exception,)):
    def retry(func):
        def wrapper(*args, **kwargs):
            error = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except exception_types as error:
                    print(f"Function failed. Retries count: #{i + 1}: {error}")
            raise error
        return wrapper
    return retry


@retry_decorator(retries=10, exception_types=(ValueError,))
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def test_unstable_function():
    unstable_function()

