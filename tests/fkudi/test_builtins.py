import pytest


def test_len():
    x = "1234"
    res = len(x)
    assert res == 4


@pytest.mark.parametrize("item, expected_length", [
    ("1234", 4),
    ([1, 2, 3, 4], 4),
    ([], 0)
])
def test_len_variouse_types(item, expected_length):
    x = item
    res = len(x)
    assert res == expected_length


def test_len_error():
    x = 145
    with pytest.raises(TypeError):
        len(x)
