from random import random
import pytest


def retry(iters):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            while total < iters:
                try:
                    return_value = func(*args, **kwargs)
                    break
                except AssertionError as msg:
                    print(msg)
                total += 1
                print("Total iterations:{}".format(total))
            return return_value
        return wrapper

    return actual_decorator


@retry(5)
def test_get_random():
    x = random()
    print(x)
    assert x <= 0.5
    return x


if __name__ == '__main__':
    test_get_random()
