from ihontaryk.homework_10.simple_callable import SimpleCallable


def test_callable(callable_class=SimpleCallable, calls=5):
    """
    verify simple callable class
    """

    a = callable_class()

    for i in range(calls):
        a()

    assert a.call_count == calls
