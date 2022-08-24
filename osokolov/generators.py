
def simple_generator(iterable):
    for i in iterable:
        yield i


def reversed_generator(iterable):
    for i in reversed(iterable):
        yield i


def cycle_generator(iterable):
    while True:
        for i in iterable:
            yield i


def ping_pong_generator(iterable):
    ...


if __name__ == "__main__":

    a = [0, 1, 2]

    # iterator = simple_generator(a)
    # b = list(iterator)
    # assert b == [0, 1, 2]
    #
    # iterator = reversed_generator(a)
    # b = list(iterator)
    # assert b == [2, 1, 0]

    iterator = cycle_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

    # iterator = ping_pong_generator(a)
    # b = [next(iterator) for _ in range(14)]
    # assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
