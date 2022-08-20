class SimpleIterator:
    def __init__(self, iterable):
        ...

    def __next__(self):
        ...


class ReversedIterator:

    def __init__(self, iterable):
        ...

    def __next__(self):
        ...


class CycleIterator:
    def __init__(self, iterable):
        ...

    def __next__(self):
        ...


class PingPongIterator:

    def __init__(self, iterable):
        ...

    def __next__(self):
        ...


if __name__ == "__main__":

    a = [0, 1, 2]

    iterator = SimpleIterator(a)
    b = list(iterator)
    assert b == [0, 1, 2]

    iterator = ReversedIterator(a)
    b = list(iterator)
    assert b == [2, 1, 0]

    iterator = CycleIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

    iterator = PingPongIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
