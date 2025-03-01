import pytest

from vpavly.m1.acceptable_password import is_acceptable_password


# 3 #
@pytest.mark.parametrize('a, expected', [
    ('test_pass', True),
    ('pass', False),
    ('qwerty1', True)
])
def test_is_acceptable_password(a, expected):
    assert is_acceptable_password(a) == expected
