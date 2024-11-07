from collections.abc import Iterator


class SimpleIterator(Iterator):

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        next_item = self.iterable[self.index]
        self.index += 1
        return next_item


class ReversedIterator(Iterator):

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable) - 1

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        next_item = self.iterable[self.index]
        self.index -= 1
        return next_item


class CycleIterator(Iterator):

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __next__(self):
        while True:
            if self.index >= len(self.iterable):
                self.index = 0
            try:
                next_item = self.iterable[self.index]
                self.index += 1
                return next_item
            except IndexError:
                break


class PingPongIterator(Iterator):

    def __init__(self, iterable):
        self.iterable = iterable
        self.is_ascending = True
        self.index = 0

    def __next__(self):
        while True:
            if self.is_ascending and self.index == len(self.iterable) - 1:
                self.is_ascending = False
                self.index = len(self.iterable) - 1
            if not self.is_ascending and self.index == 0:
                self.is_ascending = True

            try:
                next_item = self.iterable[self.index]
                self.index = (self.index + 1) if self.is_ascending else (self.index - 1)
                return next_item
            except IndexError:
                break
