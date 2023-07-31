a = [0, 1, 2]


def simple_generator(iterable):
    for item in iterable:
        yield item


def test_generators():

    iterator = simple_generator(a)
    b = list(iterator)
    assert b == [0, 1, 2]


def reversed_generator(iterable):
    for item in reversed(iterable):
        yield item


def test_reversed_generator():
    iterator = reversed_generator(a)
    b = list(iterator)
    assert b == [2, 1, 0]


def cycle_generator(iterable):
    for item in iterable:
        yield item


def test_cycle_iterator():
    iterator = cycle_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

def ping_pong_generator(iterable):
    while True:
        for item in iterable:
            yield item
        for item in reversed(iterable[1:-1]):
            yield item

def test_ping_pong_generator():
    iterator = ping_pong_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]


