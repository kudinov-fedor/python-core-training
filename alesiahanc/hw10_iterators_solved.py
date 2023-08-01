class MainIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0

    def __iter__(self):
        return self


class SimpleIterator(MainIterator):

    def __next__(self):
        if self.position < len(self.iterable):
            item = self.iterable[self.position]
            self.position += 1
            return item

        raise StopIteration


class ReversedIterator(MainIterator):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.position = len(self.iterable) - 1

    def __next__(self):
        if self.position < 0:
            raise StopIteration

        item = self.iterable[self.position]
        self.position -= 1
        return item


class CycleIterator(MainIterator):

    def __next__(self):
        if self.position >= len(self.iterable):
            self.position = 0

        item = self.iterable[self.position]
        self.position += 1
        return item


class PingPongIterator(MainIterator):

    def __init__(self, iterable):
        super().__init__(iterable)
        self.iterable = iterable
        self.forward = True
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if 0 <= self.position < len(self.iterable):
            item = self.iterable[self.position]
        else:
            # If the position is in the end or beginning, the value of self.forward is changing to opposite
            self.forward = not self.forward
            # the item goes to the beginning or the end depending on self.forward value
            self.position += 2 if self.forward else -2
            item = self.iterable[self.position]

        # Move the position forward or backward based on the direction.
        self.position += 1 if self.forward else -1
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
