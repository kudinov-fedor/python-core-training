import pytest

from kkhol.most_frequent import most_frequent


@pytest.mark.parametrize('data', 'num', [
    (('a', 'a', 'b', 'c', 'c', 'c'), 3),
    ('a', 1),
    (('b', 'b', 'c'), 2)
])
def test_most_frequent(data, num):
    assert most_frequent(data) == num
