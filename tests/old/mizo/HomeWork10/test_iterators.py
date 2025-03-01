import pytest

from mizo.iterators import SimpleIterator, ReversedIterator, CycleIterator, PingPongIterator


@pytest.mark.parametrize(["data", "expected"], [
    ([1, 2, 3], [1, 2, 3]),
    ("Hello", ["H", "e", "l", "l", "o"]),
    (range(5), [0, 1, 2, 3, 4]),
    ((10, 20, 30), [10, 20, 30]),
    ([], []),
])
def test_simple_iterator(data, expected):
    a = data
    iterator = SimpleIterator(a)
    b = list(iterator)
    assert b == expected


@pytest.mark.parametrize(["data", "expected"], [
    ([1, 2, 3], [3, 2, 1]),
    ("Hello", ["o", "l", "l", "e", "H"]),
    (range(5), [4, 3, 2, 1, 0]),
    ((10, 20, 30), [30, 20, 10]),
    ([], []),
])
def test_reversed_iterator(data, expected):
    a = data
    iterator = ReversedIterator(a)
    b = list(iterator)
    assert b == expected


@pytest.mark.parametrize(["data", "expected"], [
    ([1, 2, 3], [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]),
    ("Hello", ["H", "e", "l", "l", "o", "H", "e", "l", "l", "o"]),
    ((10, 20, 30), [10, 20, 30, 10, 20, 30, 10, 20, 30, 10])

])
def test_cycle_iterator(data, expected):
    a = data
    iterator = CycleIterator(a)
    b = [next(iterator) for _ in range(10)]
    assert b == expected


@pytest.mark.parametrize(["data", "expected"], [
    ([1, 2, 3], [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2]),
    ("Hello", ['H', 'e', 'l', 'l', 'o', 'l', 'l', 'e', 'H', 'e', 'l', 'l', 'o', 'l'])

])
def test_ping_pong_iterator(data, expected):
    a = data
    iterator = PingPongIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == expected
