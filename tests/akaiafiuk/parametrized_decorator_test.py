from akaiafiuk.parametrized_decorator import get_random, get_random_param


def test_get_random():
    assert get_random() <= 0.5


def test_get_random_parametrized():
    try:
        assert get_random_param() <= 0.5
    except TypeError:
        ...
