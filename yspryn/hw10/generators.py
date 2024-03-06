
def simple_generator(iterable):
    position = 0
    while position < len(iterable):
        item = iterable[position]
        position += 1
        yield item


def reversed_generator(iterable):
    position = len(iterable) - 1
    while position >= 0:
        item = iterable[position]
        position -= 1
        yield item


def cycle_generator(iterable):
    position = 0
    while True:
        item = iterable[position]
        if position == len(iterable) - 1:
            position = 0
        else:
            position += 1
        yield item


def ping_pong_generator(iterable):
    position = 0
    flag_forward = True

    while True:
        item = iterable[position]

        if flag_forward:
            position += 1
            if position == len(iterable):
                position -= 2
                flag_forward = False
        else:
            position -= 1
            if position < 0:
                position += 2
                flag_forward = True

        yield item
