"""
Create decorator, which would calculate how long does function run take

import time
start = time.time_ns()
print(time.time_ns() - start)
"""
import time
from operator import gt, lt, le, ge


def timer(func):
    def inner(*args, **kwargs):
        start_time = time.process_time()
        result = func(*args, **kwargs)
        print(time.process_time() - start_time)
        return result
    return inner


@timer
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


@timer
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


@timer
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


@timer
def select_sort(iterable, reverse: bool = True, key: callable = None) -> list:
    """
    Pick biggest item
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


if __name__ == "__main__":

    import random

    rand_range = tuple(random.random() for _ in range(1000))
    for f in [bubble_sort, gnome_sort, insert_sort, select_sort]:
        for rev in [True, False]:
            print(f(rand_range, reverse=rev) == sorted(rand_range, reverse=rev))

    assert bubble_sort([4,5,6,7,1]) == [7,6,5,4,1]
