from irepela.homework_10.simple_callable import SimpleCallable


def test_simple_callable():
    a = SimpleCallable()

    assert a.call_count == 0

    a()
    a()
    assert a.call_count == 2
