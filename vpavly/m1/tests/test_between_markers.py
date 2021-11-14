import pytest

from vpavly.m1.between_markers import between_markers


# 13 #
@pytest.mark.parametrize('a, b, c, expected', [
    ('What is >apple<', '>', '<', 'apple'),
    ('What is [apple]', '[', ']', 'apple'),
    ('What is ><', '>', '<', ''),
    ('<apple>', '<', '>', 'apple')
])
def test_between_markers(a, b, c, expected):
    assert between_markers(a, b, c) == expected
