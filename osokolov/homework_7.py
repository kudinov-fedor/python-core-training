"""
Create decorator, which will retry inner function multiple times untill it passes
"""

import random


def make_stable(func):
    def repeat():
        while True:
            try:
                f = func()
            except ValueError:
                continue
            return f

    return repeat


def make_stable_recursion(func):
    def repeat():
        f = None
        try:
            f = func()
        except ValueError:
            repeat()
        return f

    return repeat


@make_stable_recursion
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
