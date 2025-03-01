import pytest

from vpavly.m1.correct_sentence import correct_sentence_long


# 14 #
@pytest.mark.parametrize('a, expected', [
    ('hello, world', 'Hello, world.'),
    ('Hi, my name is Shai-Hulud.', 'Hi, my name is Shai-Hulud.'),
    ('', '')
])
def test_correct_sentence(a, expected):
    assert correct_sentence_long(a) == expected
