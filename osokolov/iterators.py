class SimpleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.iterable_length = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.iterable_length:
            elem = self.iterable[self.index]
            self.index += 1
            return elem
        raise StopIteration


class ReversedIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != 0:
            self.index -= 1
            return self.iterable[self.index]

        raise StopIteration


class CycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.iterable_length = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index < self.iterable_length:
                elem = self.iterable[self.index]
                self.index += 1
                return elem
            else:
                self.index = 0


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

    # iterator = PingPongIterator(a)
    # b = [next(iterator) for _ in range(14)]
    # assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
