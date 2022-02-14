import pytest

from odysh.easy_unpack import easy_unpack


@pytest.mark.parametrize("tuple, exp_tuple", [
    ((1, 2, 3, 4, 5, 6, 7, 9), (1, 3, 7)),
    ((6, 2, 9, 4, 3, 9), (6, 9, 3)),
    ((1, 1, 1, 1), (1, 1, 1)),
    ((6, 3, 7), (6, 7, 3)),
])
def test_easy_unpack(tuple, exp_tuple):
    assert easy_unpack(tuple) == exp_tuple


def test_negative_unpack():
    with pytest.raises(IndexError) as e:
        easy_unpack((1, 2))
    assert e.typename ==  "IndexError"