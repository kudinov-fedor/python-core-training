import random
import logging
import functools
import time

global_value = 10


def change_global_value(x: int):
    global global_value
    global_value = x
    return global_value


def get_global_value():
    return global_value


def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def add_retry_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        loop = True
        while loop:
            try:
                res = func(*args, **kwargs)
            except ValueError:
                logging.info(f'Value < 0.5 not allowed.')
            else:
                loop = False
        return res
    return wrapper


def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        res = func(*args, **kwargs)
        print(time.time_ns() - start)
        return res
    return wrapper


def memory(func):
    saved_results = {}

    @functools.wraps(func)
    def wrapper(num):
        if num not in saved_results:
            saved_results[num] = func(num)
        return saved_results[num]
    return wrapper


@memory
def fibo(num: int) -> int:
    return sum(i for i in range(num+1))







