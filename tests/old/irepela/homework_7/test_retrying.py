import pytest
import random
from irepela.homework_7.retrying import retry


def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def test_unstable_function(mocker):
    mocker.patch.object(random, 'random', side_effect=[0.1, 0.2, 0.3, 0.4, 0.55])
    wrapped = retry(3)(unstable_function)
    with pytest.raises(ValueError):
        wrapped()

    wrapped = retry()(unstable_function)
    assert wrapped() == 0.55
