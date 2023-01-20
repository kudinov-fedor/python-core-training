"""
Create decorator, which will retry inner function multiple times untill it passes
"""
import functools
import random


def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        attempt = 1
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                print(f"Attempt = {attempt}. {exc} occurs, trying again")
                attempt += 1
                continue

    return wrapper


@retry
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    print(unstable_function())
