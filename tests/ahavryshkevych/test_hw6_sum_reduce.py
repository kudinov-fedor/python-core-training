from operator import mul, add

import pytest

from ahavryshkevych.task_reduce_sum import own_reduce, own_sum


@pytest.mark.parametrize("some_list, key, default, result", [
    ([-7, -4, -2, 1, 2, 3, 4, 5, 6], mul, 1, -40320),
    ([], mul, 1, 1),
    ([-7, -4, -2, 1, 2, 3, 4, 5, 6], add, 0, 8),
    ([-7, -4, -2, 1, 2, 3, 4, 5, 6], (lambda a, b: a + b), 0, 8),
    ([], add, 0, 0)
])
def test_reduce_func(some_list, key, default, result):
    assert own_reduce(*some_list, key=key, default=default) == result


def test_sum_func():
    assert own_sum(-7, -4, -2, 1, 2, 3, 4, 5, 6) == 8
