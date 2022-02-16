import pytest

from ylond.extend_func import extend_func


@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 4], [5, 6, 7], [1, 2, 4, 5, 6, 7]),
    ([], ['cat', 'dog'], ['cat', 'dog']),
    ([], (1, 2, 85), [1, 2, 85]),
    ([], {1, 'test', 85}, [1, 85, 'test']),
    ([], {'dict': 1, 'dict1': 2}, ['dict', 'dict1']),
    ([], range(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])])
def test_extend_funct(a, b, expected):
    assert extend_func(a, b) == expected


def test_extend_error():
    a = ('$', '100')
    b = [1, 2, 3]
    with pytest.raises(AttributeError):
        extend_func(a, b)
