import random

import pytest

from obalk.home_task_7.retying import unstable_function


def test_make_stable(mocker):
    mocker.patch.object(random, 'random', return_value=0.1)

    with pytest.raises(ValueError) as er:
        unstable_function()

    assert random.random.call_count == 3
    assert "unstable_function did not retry in attempts=3" in str(er.value)


def test_make_unstable(mocker):
    mocker.patch.object(random, 'random', side_effect=[0.1, 0.49, 0.5])
    res = unstable_function()
    assert res == 0.5
