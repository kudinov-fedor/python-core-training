
def simple_generator(iterable):
    start = 0
    while start < len(iterable):
        yield iterable[start]
        start += 1


def reversed_generator(iterable):
    start = len(iterable) - 1
    while start >= 0:
        yield iterable[start]
        start -= 1


def cycle_generator(iterable):
    start = 0
    while True:
        if start >= len(iterable):
            start = 0

        yield iterable[start]
        start += 1


def ping_pong_generator(iterable):
    start = 0
    asc = True

    while True:
        item = iterable[start]
        if asc and start == len(iterable) - 1:
            asc = False
        elif asc is False and start == 0:
            asc = True

        start = start + 1 if asc else start - 1
        yield item
