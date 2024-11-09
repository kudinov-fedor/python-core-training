def custom_zip(*iterable):
    iterators = [iter(i) for i in iterable]
    try:
        while True:
            yield tuple([next(i) for i in iterators])
    except StopIteration:
        return


def custom_enumerate(iterable, start=0):
    indexes = range(start, len(iterable) + start)
    for i in custom_zip(indexes, iterable):
        yield i


def custom_filter(key, iterable):
    key = key or (lambda i: i)
    for i in iterable:
        if key(i):
            yield i


def custom_map(func, *iterables):
    for args in custom_zip(*iterables):
        yield func(*args)
