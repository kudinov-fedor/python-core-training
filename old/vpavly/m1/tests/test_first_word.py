import pytest

from vpavly.m1.first_word import first_word


# 2 #
@pytest.mark.parametrize('a, expected', [
    ('Hello world', 'Hello'),
    ('', ''),
    ('1', '1')
])
def test_first_word(a, expected):
    assert first_word(a) == expected
