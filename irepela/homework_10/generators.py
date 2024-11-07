
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

        try:
            yield iterable[index]
            index += 1
        except IndexError:
            break


def ping_pong_generator(iterable):
    index = 0
    is_ascending = True
    while True:
        if is_ascending and index == len(iterable) - 1:
            is_ascending = False
            index = len(iterable) - 1
        if not is_ascending and index == 0:
            is_ascending = True

        try:
            yield iterable[index]
            index = (index + 1) if is_ascending else (index - 1)
        except IndexError:
            break
