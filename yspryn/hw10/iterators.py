class SimpleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < len(self.iterable):
            item = self.iterable[self.position]
            self.position += 1
            return item
        raise StopIteration


class SimpleIterator2:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        position = 0
        while position < len(self.iterable):
            item = self.iterable[position]
            position += 1
            yield item
        return


class ReversedIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.position = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= 0:
            item = self.iterable[self.position]
            self.position -= 1
            return item
        raise StopIteration


class CycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration

        item = self.iterable[self.position]
        if self.position == len(self.iterable) - 1:
            self.position = 0
        else:
            self.position += 1
        return item


class PingPongIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.position = 0
        self.flag_forward = True

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterable:
            raise StopIteration

        item = self.iterable[self.position]

        if self.flag_forward:
            self.position += 1
            if self.position == len(self.iterable):
                self.position -= 2
                self.flag_forward = False
        else:
            self.position -= 1
            if self.position < 0:
                self.position += 2
                self.flag_forward = True

        return item
