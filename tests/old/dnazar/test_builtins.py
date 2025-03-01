import pytest


def test_max():
    x = (-1, -28, 11, -5, 0.6, True)
    res = max(x)
    assert res == 11


@pytest.mark.parametrize("item, expected_max", [
    ("1234", "4"),
    (["123", "12"], "123"),
    ([5, 3, 8, 4], 8),
    ((1, 4, 2, 23, 6), 23),
    ([True, False], True)
])
def test_max_various_types(item, expected_max):
    x = item
    res = max(x)
    assert res == expected_max


def test_max_value_error():
    x = []
    with pytest.raises(ValueError):
        max(x)

def test_max_type_error():
    x = None
    with pytest.raises(TypeError):
        max(x)
