from irepela.homework_10.generators import simple_generator, reversed_generator, cycle_generator, ping_pong_generator


def test_generators():
    a = [0, 1, 2]

    iterator = simple_generator(a)
    b = list(iterator)
    assert b == [0, 1, 2]

    iterator = reversed_generator(a)
    b = list(iterator)
    assert b == [2, 1, 0]

    iterator = cycle_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]

    iterator = ping_pong_generator(a)
    b = [next(iterator) for _ in range(14)]
    assert b == [0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1]

    a = [0, 1, 2, 3, 4, 5]
    iterator = ping_pong_generator(a)
    b = [next(iterator) for _ in range(15)]
    assert b == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
