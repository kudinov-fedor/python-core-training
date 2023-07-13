"""
Create decorator, which will retry inner function multiple times untill it passes
"""


import random


# creating new func that use existing func as argument and returns updated func
def retry(func):
    #  inner function calls original one, until original passes
    def inner(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                print(error)
                continue

    return inner


@retry
def unstable_function():
    res = random.random()
    print(res)
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    res = unstable_function()
    print(res)
