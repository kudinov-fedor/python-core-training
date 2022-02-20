import pytest


def test_len():
    x = "23456"
    res = len(x)
    assert res == 5


@pytest.mark.parametrize("item, expected_length", [
    ("23456", 5),
    ([1, 2, 3, 6, 8], 5),
    ([], 0)
])
def test_len_list_various_types(item, expected_length):
    x = item
    res = len(x)
    assert res == expected_length


def test_len_error():
    x = 145
    with pytest.raises(TypeError):
        len(x)
