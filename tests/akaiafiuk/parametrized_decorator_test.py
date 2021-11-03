from akaiafiuk.parametrized_decorator import get_random, get_random_param


def test_get_random():
    assert get_random() <= 0.5


def test_get_random_parametrized():
    assert get_random_param() <= 0.5 or get_random_param() is None
