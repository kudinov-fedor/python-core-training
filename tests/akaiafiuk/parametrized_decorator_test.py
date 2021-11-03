from akaiafiuk.parametrized_decorator import get_random, get_random_param


def test_get_random():
    assert get_random() <= 0.5


def test_get_random_parametrized():
    # todo: try to add test that takes into account the fact that exception can be raised
    assert get_random_param() <= 0.5
