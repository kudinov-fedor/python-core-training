"""
Create decorator, which will retry inner function multiple times until it passes
"""
import random


def retry_func(func, retries=1):
    def wrapper(*args, **kwargs):
        for _ in range(retries):
            while func:
                try:
                    func(*args, **kwargs)
                    return
                except ValueError as error:
                    print(error)
                    continue

    return wrapper


@retry_func
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    print(res)
    return


if __name__ == '__main__':
    print(unstable_function())
