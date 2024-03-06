from yspryn.hw10.generators import simple_generator, reversed_generator, cycle_generator, ping_pong_generator

a = [0, 1, 2]


def test_simple_generator():
    iterator = simple_generator(a)
    b = list(iterator)
    assert b == [0, 1, 2]


def test_reversed_generator():
    iterator = reversed_generator(a)
    b = list(iterator)
    assert b == [2, 1, 0]


def test_cycle_generator():
    iterator = cycle_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]


def test_ping_pong_generator():
    iterator = ping_pong_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
