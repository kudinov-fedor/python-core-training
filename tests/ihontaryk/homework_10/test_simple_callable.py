import pytest

from ihontaryk.homework_10.simple_callable import SimpleCallable


@pytest.mark.parametrize('callable_class, calls', [(SimpleCallable, 5)])
def test_catcher(callable_class, calls):
    """
    verify simple callable class
    """
    a = callable_class()

    for i in range(calls):
        a()

    assert a.call_count == calls
