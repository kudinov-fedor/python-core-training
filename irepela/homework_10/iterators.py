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
        if self.index >= len(self.iterable):
            self.index = 0

        next_item = self.iterable[self.index]
        self.index += 1
        return next_item


class PingPongIterator(Iterator):

    def __init__(self, iterable):
        self.iterable = iterable
        self.change_order = False
        self.index = 0

    def __next__(self):
        if self.index == len(self.iterable) - 1:
            self.change_order = True
        if self.index == 0:
            self.change_order = False

        next_item = self.iterable[self.index]
        increment = -1 if self.change_order else 1
        self.index += increment
        return next_item
