"""
Create decorator, which will retry inner function multiple times until it passes
"""

import random


def retry_func(func):
    def wrapper():
        while func:
            try:
                func()
                break
            except ValueError as error:
                print(error)
    return wrapper


@retry_func
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    print(res)


if __name__ == '__main__':
    print(unstable_function())
