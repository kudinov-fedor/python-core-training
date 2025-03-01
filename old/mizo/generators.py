a = [0, 1, 2]


def simple_generator(iterable):
    length = len(iterable)
    index = 0
    while index < length:
        yield iterable[index]
        index += 1


def test_simple_generator():
    iterator = simple_generator(a)
    b = list(iterator)
    assert b == [0, 1, 2]


def reversed_generator(iterable):
    length = len(iterable)
    index = length - 1
    while index >= 0:
        yield iterable[index]
        index -= 1


def test_reversed_generator():
    iterator = reversed_generator(a)
    b = list(iterator)
    assert b == [2, 1, 0]


def cycle_generator(iterable):
    n = len(iterable)
    while True:
        for i in range(n):
            yield iterable[i]


def test_cycle_iterator():
    iterator = cycle_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]


def ping_pong_generator(iterable):
    length = len(iterable)
    while True:
        for i in range(length):
            yield iterable[i]
        for i in range(length - 2, 0, -1):
            yield iterable[i]


def test_ping_pong_generator():
    iterator = ping_pong_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
