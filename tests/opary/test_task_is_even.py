from opary.task_is_even import is_even

import pytest


@pytest.mark.parametrize("data, result", [
    (270, True),
    (39, False),
    (1234567890, True),
    (35792, True),
    (0, True),
    (-572, True)
])
def test_is_even(data, result):
    assert is_even(data) == result
