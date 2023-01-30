from operator import add


def zip_new(*iterables):
    iterators = [iter(i) for i in iterables]
    try:
        while True:
            yield tuple([next(i) for i in iterators])
    except StopIteration:
        return


def enumerate_new(iterable, start: int = 0):
    indexes = range(start, len(list(iterable)) + start)
    yield from zip_new(indexes, iterable)


def filter_new(function_or_none, iterable):
    function_or_none = function_or_none or (lambda value: value)
    for i in iterable:
        if function_or_none(i):
            yield i


def map_new(function, *iterables):
    for parameters in zip_new(*iterables):
        yield function(*parameters)


if __name__ == '__main__':
    gen1 = (value for value in (1, 2))
    gen2 = (value for value in (1, 2))
    seq2 = [1, 2, 3]
    seq3 = [3, 4]

    # zip
    assert list(zip(gen1, seq2, seq3)) == list(zip_new(gen2, seq2, seq3))
    assert list(zip(seq2, seq3)) == list(zip_new(seq2, seq3))
    assert list(zip(seq2)) == list(zip_new(seq2))
    str1 = "223"
    str2 = "1234"

    assert list(zip_new(str1, str2)) == list(zip(str1, str2))
    assert list(zip_new(str1)) == list(zip(str1))

    # enumerate
    assert list(enumerate_new(seq2)) == list(enumerate(seq2))
    assert list(enumerate_new(seq2, 1)) == list(enumerate(seq2, 1))
    assert list(enumerate_new(gen1, 1)) == list(enumerate(gen2, 1))

    # filter
    assert list(filter_new(None, str2)) == list(filter(None, str2))
    assert list(filter_new(None, seq2)) == list(filter(None, seq2))
    assert list(filter_new(None, gen1)) == list(filter(None, gen2))
    condition = lambda i: int(i) < 2
    assert list(filter_new(condition, str2)) == list(filter(condition, str2))
    assert list(filter_new(condition, seq2)) == list(filter(condition, seq2))
    assert list(filter_new(condition, gen1)) == list(filter(condition, gen2))

    # map
    func = lambda i: i + 1
    assert list(map_new(func, seq2)) == list(map(func, seq2))
    assert list(map_new(add, gen1, seq2)) == list(map(add, gen1, seq2))
