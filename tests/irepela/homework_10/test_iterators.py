from irepela.homework_10.iterators import SimpleIterator, ReversedIterator, CycleIterator, PingPongIterator


def test_iterators():
    a = [0, 1, 2]

    iterator = SimpleIterator(a)
    b = list(iterator)
    assert b == [0, 1, 2]

    iterator = ReversedIterator(a)
    b = list(iterator)
    assert b == [2, 1, 0]

    iterator = CycleIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

    iterator = PingPongIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]

    a = [0, 1, 2, 3, 4, 5]
    iterator = PingPongIterator(a)
    b = [next(iterator) for _ in range(15)]
    assert b == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
