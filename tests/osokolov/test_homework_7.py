import pytest
from osokolov.homework_7 import unstable_function, make_stable, make_stable_recursion


def test_make_stable(mocker):
    mocker.patch.object(unstable_function, 'random',  return_value=0.6)

    assert unstable_function() == 0.6
