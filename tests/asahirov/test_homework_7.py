import random
from operator import gt, lt, le, ge
import time

"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""


def remember_answer(func):
    answer = {}

    def remember(*args):
        if args in answer:
            return answer[args]
        else:
            result = func(*args)
            answer[args] = result
            return result

    return remember


@remember_answer
def fibo(n: int):
    """
    Count fibonache numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """
    if n < 3:
        return [0, 1, 2][n]
    return fibo(n - 1) + fibo(n - 2)


def test_remember_answer_decorator():
    for i in range(10):
        print(fibo(i))


# ----------------------------------------------------------------------------------
"""
Create decorator, which will retry inner function multiple times untill it passes
"""


def retry_decorator(retries: int = 5):
    def retry(func):
        def wrapper():
            for i in range(retries):
                try:
                    return func()
                except ValueError:
                    print(f"Function failed. Retry #{i + 1}")
            raise ValueError(f"Function failed. Retries count: {retries}")
        return wrapper
    return retry


@retry_decorator(retries=10)
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def test_unstable_function():
    unstable_function()


# ----------------------------------------------------------------------------------
"""
Create decorator, which would calculate how long does function run take

import time
start = time.time_ns()
print(time.time_ns() - start)
"""


def stopwatch(func):
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        result = func(*args, **kwargs)
        end = time.time_ns()
        run_time = (end - start) / 1000000000
        print(f"Function {func} runtime is {run_time} seconds")
        return result
    return wrapper


@stopwatch
def bubble_sort(iterable, reverse: bool = True, key: callable = None) -> list:
    """
    go item by item and swap them if left is bigger than right
    """
    args = list(iterable)
    compare = lt if reverse else gt
    key = key or (lambda x: x)

    is_sorted = False
    limit = len(args) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(limit):
            key_1 = key(args[i])
            key_2 = key(args[i + 1])
            if compare(key_1, key_2):  # main compare function
                args[i], args[i + 1] = args[i + 1], args[i]
                is_sorted = False
        limit -= 1
    return args


@stopwatch
def gnome_sort(iterable, reverse: bool = True, key: callable = None) -> list:
    """
    grab an item and drag it to place, where closest is bigger than this
    """
    args = list(iterable)
    compare = lt if reverse else gt
    key = key or (lambda x: x)

    length = len(args)
    position = 1
    last_position = position

    while position != length:
        if compare(key(args[position - 1]), key(args[position])):
            args[position], args[position - 1] = args[position - 1], args[position]
            if position > 1:
                position -= 1
                continue

        position = last_position + 1
        last_position = position
    return args


@stopwatch
def insert_sort(iterable, reverse: bool = True, key: callable = None) -> list:
    """
    Pick any item
    and insert into correct place in new collection
    """
    args = list(iterable)
    compare = le if reverse else ge
    key = key or (lambda x: x)

    for i in range(1, len(args)):
        if compare(key(args[i]), key(args[i - 1])):
            continue

        el = args.pop(i)
        for j in range(i):
            if compare(key(args[j]), key(el)):
                args.insert(j, el)
                break
        else:
            args.insert(i, el)

    return args


@stopwatch
def select_sort(iterable, reverse: bool = True, key: callable = None) -> list:
    """
    Pick the biggest item
    and insert to the end into new collection
    """
    args = list(iterable)
    compare = lt if reverse else gt
    key = key or (lambda x: x)

    res = []
    while args:
        extreme_el = args[0]
        for i in range(1, len(args)):
            if compare(key(extreme_el), key(args[i])):
                extreme_el = args[i]
        args.remove(extreme_el)
        res.append(extreme_el)
    return res


def test_sorting():
    rand_range = tuple(random.random() for _ in range(1000))
    for f in [bubble_sort, gnome_sort, insert_sort, select_sort]:
        for rev in [True, False]:
            print(f(rand_range, reverse=rev) == sorted(rand_range, reverse=rev))
