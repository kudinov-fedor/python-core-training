from irepela.homework_7 import caching


def test_caching(mocker):
    spy = mocker.spy(caching, "fibo")
    caching.fibo(5)
    assert spy.call_count == 7
    assert spy.spy_return == 8
