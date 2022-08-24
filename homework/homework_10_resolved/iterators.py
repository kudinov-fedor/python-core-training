class Iterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0

    def __iter__(self):
        return self


class SimpleIterator(Iterator):

    def __next__(self):
        if self.position >= len(self.iterable):
            raise StopIteration

        item = self.iterable[self.position]
        self.position += 1
        return item


class ReversedOperator(Iterator):

    def __init__(self, iterable):
        super().__init__(iterable)
        self.position = len(self.iterable) - 1

    def __next__(self):
        if self.position < 0:
            raise StopIteration

        item = self.iterable[self.position]
        self.position -= 1
        return item


class CycleIterator(Iterator):

    def __next__(self):
        if self.position >= len(self.iterable):
            self.position = 0

        item = self.iterable[self.position]
        self.position += 1
        return item


class PingPongIterator(Iterator):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.ascending = True

    def __next__(self):
        item = self.iterable[self.position]
        if self.ascending and self.position == len(self.iterable) - 1:
            self.ascending = False
        elif self.ascending is False and self.position == 0:
            self.ascending = True

        self.position = self.position + 1 if self.ascending else self.position - 1
        return item


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
