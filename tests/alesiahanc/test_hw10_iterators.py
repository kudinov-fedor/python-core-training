from alesiahanc.hw10_iterators_solved import SimpleIterator, ReversedIterator, CycleIterator, PingPongIterator
import pytest


@pytest.mark.parametrize(["data", "expected"], [
    ([0, 1, 2], [0, 1, 2]),
    ("qwerty", ['q', 'w', 'e', 'r', 't', 'y']),
    ((0, 1, 2), [0, 1, 2])
])
def test_simple_iterator(data, expected):
    a = data

    iterator = SimpleIterator(a)
    b = list(iterator)
    assert b == expected


@pytest.mark.parametrize(["data", "expected"], [
    ([0, 1, 2], [2, 1, 0]),
    ("qwerty", ['y', 't', 'r', 'e', 'w', 'q']),
    ((0, 1, 2), [2, 1, 0])
])
def test_reversed_iterator(data, expected):
    a = data

    iterator = ReversedIterator(a)
    b = list(iterator)
    assert b == expected


@pytest.mark.parametrize(["data", "range_number", "expected"], [
    ([0, 1, 2], 14, [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]),
    ("qwerty", 14, ['q', 'w', 'e', 'r', 't', 'y', 'q', 'w', 'e', 'r', 't', 'y', 'q', 'w']),
    ((0, 1, 2), 14, [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1])
])
def test_cycle_iterator(data, range_number, expected):
    a = data

    iterator = CycleIterator(a)
    b = [next(iterator) for _ in range(range_number)]
    assert b == expected


@pytest.mark.parametrize(["data", "range_number", "expected"], [
    ([0, 1, 2], 14, [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]),
    ("qwerty", 14, ['q', 'w', 'e', 'r', 't', 'y', 't', 'r', 'e', 'w', 'q', 'w', 'e', 'r']),
    ((0, 1, 2), 14, [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1])
])
def test_cycle_iterator(data, range_number, expected):
    a = data

    iterator = PingPongIterator(a)
    b = [next(iterator) for _ in range(range_number)]
    assert b == expected
