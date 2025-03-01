import pytest
from alesiahanc.hw10_callable_solved import SimpleCallable


def test_call_counts():
    a = SimpleCallable()
    assert a.call_count == 0
    a()
    a()
    assert a.call_count == 2
