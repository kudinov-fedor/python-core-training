class Iterator:
    def __init__(self, iterable):
        self._position = -1
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        self._position += 1
        if self._position >= len(self.iterable):
            raise StopIteration
        return self.iterable[self._position]

    @property
    def position(self):
        return self._position + 1


class SimpleIterator(Iterator):
    ...


class ReversedIterator(Iterator):
    def __init__(self, iterable):
        super().__init__(iterable)
        self._position = len(iterable)

    def __next__(self):
        self._position -= 1
        if self._position < 0:
            raise StopIteration
        return self.iterable[self._position]


class CycleIterator(Iterator):
    def __next__(self):
        self._position += 1
        if self._position >= len(self.iterable):
            self._position = 0
        return self.iterable[self._position]


class PingPongIterator(Iterator):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.ascending = True

    def __next__(self):
        self._position += self.component
        if self._position >= len(self.iterable) or self._position < 0:
            self.ascending = False if self.ascending else True
            self._position += 2 * self.component
        return self.iterable[self._position]

    @property
    def component(self):
        return 1 if self.ascending else -1


class CustomZip(Iterator):
    def __init__(self, *args):
        self._position = -1
        self.iterators = args

    def __next__(self):
        self._position += 1
        try:
            return tuple(i[self._position] for i in self.iterators)
        except IndexError:
            raise StopIteration


class CustomEnumerate(Iterator):
    def __next__(self):
        self._position += 1
        if self._position >= len(self.iterable):
            raise StopIteration
        return self._position, self.iterable[self._position]


class CustomFilter(Iterator):
    def __init__(self, function=None, iterable=None):
        self._position = -1
        self.function = function
        self.iterable = iterable

    def __next__(self):
        while True:
            self._position += 1
            if self._position >= len(self.iterable):
                raise StopIteration
            if self.function(self.iterable[self._position]):
                return self.iterable[self._position]


class CustomMap(CustomFilter):
    def __next__(self):
        self._position += 1
        if self._position >= len(self.iterable):
            raise StopIteration
        return self.function(self.iterable[self._position])


if __name__ == '__main__':
    iterator = CustomZip('1234', 'abcde')
    x = list(iterator)
    assert x == [('1', 'a'), ('2', 'b'), ('3', 'c'), ('4', 'd')]

    iterator = CustomEnumerate('abcd')
    x = list(iterator)
    assert x == [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

    iterator = CustomFilter(lambda p: p > 5, [i for i in range(10)])
    x = list(iterator)
    assert x == [6, 7, 8, 9]

    iterator = CustomMap(lambda p: p + 1, [i for i in range(10)])
    x = list(iterator)
    assert x == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
