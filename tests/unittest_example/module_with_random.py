from random import random


def my_func_returns_random():
    return random()


class ClassWithConnection:
    def __init__(self, address):
        self.conn = self.connect(address)

    def connect(self, address):
        raise ConnectionError
