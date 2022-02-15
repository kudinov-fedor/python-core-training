import pytest

from odysh.backward_string import backward_string


@pytest.mark.parametrize('string, reversed', [
    ('val', 'lav'),
    ('  ', '  '),
    ('ohho', 'ohho'),
    ('123456789', '987654321')
])
def test_backward_string(string, reversed):
    assert backward_string(string) == reversed


def test_negative_backward_string():
    assert backward_string('ab') != 'ab'
