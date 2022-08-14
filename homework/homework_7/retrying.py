"""
Create decorator, which will retry inner function multiple times untill it passes
"""


import random


def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res
