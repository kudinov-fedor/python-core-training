from irepela.homework_7.caching import cache
from tests.irepela.homework_7 import test_data


def test_caching_decorator(mocker):
    # spy my_func
    spy = mocker.spy(test_data, "my_func")
    wrapped = cache(test_data.my_func)
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(2) == 4
    assert wrapped(4) == 8
    assert spy.call_count == 2
