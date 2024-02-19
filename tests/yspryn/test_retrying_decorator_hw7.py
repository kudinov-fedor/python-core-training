import pytest
import random
from yspryn.hw7.retrying import unstable_function


def test_my_function(mocker):
    mocker.patch.object(random, 'random', return_value=0.6)
    assert unstable_function() == 0.6

    mocker.patch.object(random, 'random', side_effect=[0.4, 0.3, 0.2, 0.25, 0.6])
    assert unstable_function() == 0.6
    assert random.random.call_count == 5

    mocker.patch.object(random, 'random', side_effect=[0.1, 0.15, 0.14, 0.2, 0.33, 0.49])
    with pytest.raises(ValueError):
        unstable_function()
    assert random.random.call_count == 6
