from yspryn.hw10.iterators import SimpleIterator, SimpleIterator2, CycleIterator, PingPongIterator, ReversedIterator

a = [0, 1, 2]
def test_SimpleIterator():
    iterator = SimpleIterator(a)
    b = list(iterator)
    assert b == [0, 1, 2]

def test_SimpleIterator2():
    iterator = SimpleIterator2(a)
    b = list(iterator)
    assert b == [0, 1, 2]


def test_ReversedIterator():
    iterator = ReversedIterator(a)
    b = list(iterator)
    assert b == [2, 1, 0]


def test_CycleIterator():
    iterator = CycleIterator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

a1 = [0,1,2,3]
def test_PingPongIterator():
    iterator = PingPongIterator(a1)
    b = [next(iterator) for _ in range(14)]
    print(b)
    # assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]

