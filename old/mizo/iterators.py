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


class ReversedIterator(Iterator):

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
        if self.position in range(len(self.iterable)):
            item = self.iterable[self.position]
            self.position += 1 if self.ascending else -1
            if self.position == 0 or self.position == len(self.iterable) - 1:
                self.ascending = not self.ascending
            return item
        else:
            raise StopIteration
