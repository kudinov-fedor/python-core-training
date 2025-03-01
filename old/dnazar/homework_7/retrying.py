"""
Create decorator, which will retry inner function multiple times until it passes
"""


import random


def unstable_function_dec(func):
    def wrapper():
        while True:
            try:
                return func()
            except ValueError:
                continue
    return wrapper


@unstable_function_dec
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    print(unstable_function())
