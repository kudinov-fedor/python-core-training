"""
Create decorator, which will retry inner function multiple times untill it passes
"""

import random


def retry_unstable_function(func):
    def retry():
        while True:
            try:
                return func()
            except ValueError as error:
                print(f"Retrying unstable_function {error}")
                continue

    return retry


@retry_unstable_function
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    value = unstable_function()
    print(value)
    assert value > 0.5
