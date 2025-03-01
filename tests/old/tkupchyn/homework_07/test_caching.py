from tkupchyn.homework_07.caching import caching, fibo


def test_caching_decorator(mocker):
    mocker = mocker.MagicMock(side_effect=fibo)
    wrapped = caching(mocker)

    assert wrapped(5) == 5
    assert wrapped(6) == 8
    assert wrapped(7) == 13
    assert wrapped(6) == 8
    assert wrapped(6) == 8
    assert wrapped(6) == 8
    assert mocker.call_count == 3
