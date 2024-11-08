
def simple_generator(iterable):
    index = 0
    while index < len(iterable):
        yield iterable[index]
        index += 1


def reversed_generator(iterable):
    index = len(iterable) - 1
    while index >= 0:
        yield iterable[index]
        index -= 1


def cycle_generator(iterable):
    index = 0
    while True:
        if index >= len(iterable):
            index = 0

        yield iterable[index]
        index += 1


def ping_pong_generator(iterable):
    index = 0
    change_order = False
    while True:
        if index == len(iterable) - 1:
            change_order = True
        if index == 0:
            change_order = False
        yield iterable[index]
        increment = -1 if change_order else 1
        index += increment
