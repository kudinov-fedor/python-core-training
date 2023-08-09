class Iterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0

    def __iter__(self):
        return self


class SimpleIterator(Iterator):

    def __next__(self):
        while self.position < len(self.iterable):
            item = self.iterable[self.position]
            self.position += 1
            return item
        raise StopIteration


class ReversedIterator(Iterator):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.position = 1

    def __next__(self):
        while self.position <= len(self.iterable):
            item = self.iterable[-self.position]
            self.position += 1
            return item
        raise StopIteration


class CycleIterator(Iterator):

    def __next__(self):
        while True:
            if self.position == len(self.iterable):
                self.position = 0
            item = self.iterable[self.position]
            self.position += 1
            return item


class PingPongIterator(Iterator):

    def __next__(self):
        reverse_order = [self.iterable[i] for i in range(len(self.iterable) -2, 0, -1)]
        pingpong_row = self.iterable + reverse_order
        while True:
            if self.position == len(pingpong_row):
                self.position = 0
            item = pingpong_row[self.position]
            self.position += 1
            return item
