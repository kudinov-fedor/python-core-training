import random
import logging


def retrying(func):

    def retrying_sub(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as log:
                logging.error(log)
                continue

    return retrying_sub


@retrying
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def test_unstable_function():
    res = []
    for i in range(100):
        res.append(unstable_function())
    assert len(res) == 100
