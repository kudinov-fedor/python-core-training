import pytest

cat_tuple = ("c", "a", "t")
dog_tuple = ("d", "o", "g")
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize("start, end, step, collection, expected", [
    (0, 2, 1, cat_tuple, ("c", "a")),
    (2, 0, -1, dog_tuple, ("g", "o")),
    (2, 5, 1, test_list, [3, 4, 5]),
])
def test_sequence_slice(start, end, step, collection, expected):
    assert collection[start:end:step] == expected


def test_sequence_compare():
    assert cat_tuple < dog_tuple
