import pytest
from tkupchyn.homework_02.multiply_two import multiply_two_ints


@pytest.mark.parametrize('a,b, result', [
    (0, 1, 0),
    (1, 2, 2),
    (3, 4, 12),
    (5, 6, 30),
    (7, 8, 56)])
def test_multiply_two(a, b, result):
    assert multiply_two_ints(a, b) == result
