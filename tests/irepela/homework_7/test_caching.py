from irepela.homework_7 import caching


def test_caching_decorator(mocker):
    # spy my_func
    spy = mocker.spy(caching, "my_func")
    wrapped = caching.cache(caching.my_func)
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(4) == 8
    assert spy.call_count == 2
