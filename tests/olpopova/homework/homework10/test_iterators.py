import pytest

from olpopova.homework.homework10.iterators import SimpleIterator, ReversedIterator, CycleIterator, PingPongIterator


@pytest.mark.parametrize(['iterator_type', 'expected'], [
    (SimpleIterator, [0, 1, 2]),
    (ReversedIterator, [2, 1, 0]),
])
def test_simple_iterators(iterator_type, expected):
    a = [0, 1, 2]
    iterator = iterator_type(a)
    b = list(iterator)
    assert b == expected


@pytest.mark.parametrize(['iterator_type', 'sequence', 'expected'], [
    (CycleIterator, [0, 1, 2], [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]),
    (PingPongIterator, [0, 1, 2], [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]),
    (PingPongIterator, [4, 6, 7, 10, 555], [4, 6, 7, 10, 555, 10, 7, 6, 4, 6, 7, 10, 555, 10]),
])
def test_complex_iterators(iterator_type, sequence, expected):
    iterator = iterator_type(sequence)
    b = [next(iterator) for _ in range(14)]
    assert b == expected
