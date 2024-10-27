from irepela.homework_7.caching import cache


def test_caching_decorator(mocker):
    my_func = mocker.MagicMock(side_effect=lambda a: a * 2)
    wrapped = cache(my_func)

    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(4) == 8
    assert my_func.call_count == 2
