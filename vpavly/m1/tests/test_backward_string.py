import pytest

from vpavly.m1.backward_string import backward_string_w_reversed, backward_string_w_slice


# 6 #
@pytest.mark.parametrize('a, expected', [
    ('asd', 'dsa'),
    ('a', 'a'),
    ('123', '321')
])
def test_backward_string(a, expected):
    assert backward_string_w_reversed(a) and backward_string_w_slice(a) == expected
