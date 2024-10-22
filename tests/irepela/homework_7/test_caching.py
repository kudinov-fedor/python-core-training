from irepela.homework_7.caching import cache


def test_caching_decorator(mocker):
    mocker.my_func = lambda a: a * 2

    # spy my_func
    spy = mocker.spy(mocker, "my_func")
    wrapped = cache(mocker.my_func)
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(4) == 8
    assert spy.call_count == 2
