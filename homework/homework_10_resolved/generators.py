
def simple_generator(iterable):
    position = 0
    while position < len(iterable):
        yield iterable[position]
        position += 1


def reversed_generator(iterable):
    position = len(iterable) - 1
    while position >= 0:
        yield iterable[position]
        position -= 1


def cycle_generator(iterable):
    position = 0
    while True:
        if position >= len(iterable):
            position = 0

        yield iterable[position]
        position += 1


def ping_pong_generator(iterable):
    position = 0
    ascending = True

    while True:
        item = iterable[position]
        if ascending and position == len(iterable) - 1:
            ascending = False
        elif ascending is False and position == 0:
            ascending = True

        position = position + 1 if ascending else position - 1
        yield item


if __name__ == "__main__":

    a = [0, 1, 2]

    iterator = simple_generator(a)
    b = list(iterator)
    assert b == [0, 1, 2]

    iterator = reversed_generator(a)
    b = list(iterator)
    assert b == [2, 1, 0]

    iterator = cycle_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

    iterator = ping_pong_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
