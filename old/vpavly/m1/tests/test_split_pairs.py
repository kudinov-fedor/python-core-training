import pytest

from vpavly.m1.split_pairs import split_pairs


# 11 #
@pytest.mark.parametrize('a, expected', [
    ('abcdef', ['ab', 'cd', 'ef']),
    ('abc', ['ab', 'c_']),
    ('', [])
])
def test_split_pairs(a, expected):
    assert split_pairs(a) == expected
