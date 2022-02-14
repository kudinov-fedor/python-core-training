import pytest

from fkudi.task_multiply import mult_two


@pytest.mark.parametrize("a, b, expected", [
    (4, 3, 12),
    (3, 2, 6),
    (1, 0, 0),
])
def test_mult_two(a, b, expected):
    assert mult_two(a, b) == expected
