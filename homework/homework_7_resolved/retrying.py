"""
Create decorator, which will retry inner function multiple times untill it passes
"""


import random


def retry(func):

    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)  # to check if errors happened
                continue

    return wrapper


@retry
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    res = unstable_function()
    print(res)
