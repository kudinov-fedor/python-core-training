from irepela.homework_7.retrying import unstable_function
import random


def test_unstable_function(mocker):
    mocker.patch.object(random, 'random', side_effect=[0.1, 0.2, 0.3, 0.4, 0.55])
    assert unstable_function() == 0.55
    assert random.random.call_count == 5
