import pytest
from mizo.task_even import is_even


@pytest.mark.parametrize("num, expected", [
    (12, True),
    (13, False),
    (25, False)
])
def test_is_even(num, expected):
    assert is_even(num) is expected
