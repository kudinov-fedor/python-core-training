import pytest
from yspryn.hw7 import caching


def test_remember_answer_decorator(mocker):
    spy = mocker.spy(caching, 'fibo')
    caching.fibo(3)
    assert spy.call_count == 3
    assert spy.spy_return == 3
    caching.fibo(6)
    assert spy.call_count == 10
    assert spy.spy_return == 13
