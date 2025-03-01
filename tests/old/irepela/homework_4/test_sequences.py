import pytest

cat_tuple = ("c", "a", "t")
dog_tuple = ("d", "o", "g")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize("test_slice, collection, expected", [
    (slice(0, 2, 1), cat_tuple, ("c", "a")),
    (slice(2, 0, -1), dog_tuple, ("g", "o")),
    (slice(2, 5, 1), test_list, [3, 4, 5]),
])
def test_sequence_slice(test_slice, collection, expected):
    assert collection[test_slice] == expected


def test_sequence_compare():
    assert cat_tuple < dog_tuple
