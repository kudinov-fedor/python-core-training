from operator import add
from typing import Sequence, Collection, Iterable

zip, enumerate, filter, map


def zip_new(*iterables):
    shortest_iterable = min(iterables, key=len)
    for i in range(len(shortest_iterable)):
        yield tuple(b[i] for b in iterables)


def enumerate_new(iterable, start: int = 0):
    for i in range(len(iterable)):
        yield start + i, iterable[i]


def enumerate_new_2(iterable, start: int = 0):
    indexes = range(start, len(iterable) + start)
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
    seq1 = [2, 3]
    seq2 = [1, 2, 3]
    seq3 = [3, 4]

    # zip
    assert list(zip(seq1, seq2, seq3)) == list(zip_new(seq1, seq2, seq3))
    assert list(zip(seq2, seq3)) == list(zip_new(seq2, seq3))
    assert list(zip(seq2)) == list(zip_new(seq2))
    str1 = "223"
    str2 = "1234"

    assert list(zip_new(str1, str2)) == list(zip(str1, str2))
    assert list(zip_new(str1)) == list(zip(str1))

    # enumerate
    assert list(enumerate_new(seq2)) == list(enumerate(seq2))
    assert list(enumerate_new_2(seq2)) == list(enumerate(seq2))
    assert list(enumerate_new(seq2, 1)) == list(enumerate(seq2, 1))
    assert list(enumerate_new_2(seq2, 1)) == list(enumerate(seq2, 1))

    # filter
    assert list(filter_new(None, str2)) == list(filter(None, str2))
    assert list(filter_new(None, seq2)) == list(filter(None, seq2))
    condition = lambda i: int(i) < 2
    assert list(filter_new(condition, str2)) == list(filter(condition, str2))
    assert list(filter_new(condition, seq2)) == list(filter(condition, seq2))

    # map
    func = lambda i: i + 1
    assert list(map_new(func, seq2)) == list(map(func, seq2))
    assert list(map_new(add, seq1, seq2)) ==  list(map(add, seq1, seq2))
