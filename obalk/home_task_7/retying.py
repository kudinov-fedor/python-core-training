"""
Create decorator, which will retry inner function multiple times untill it passes
"""
import functools
import random


def retry(attempts):
    def func_wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            while attempt <= attempts:
                try:
                    print(f"Attempt = {attempt}.")
                    return func(*args, **kwargs)
                except Exception as exc:
                    print(f"{exc} occurs, trying again.")
                    attempt += 1
            else:
                raise ValueError(f"{func.__name__} did not retry in {attempts=}")

        return wrapper

    return func_wraps


@retry(1)
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    print(unstable_function())
