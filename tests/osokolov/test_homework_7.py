import random

import pytest

from osokolov.homework_7 import unstable_function


def test_make_stable(mocker):
    mocker.patch.object(random, 'random', return_value=0.2)
    with pytest.raises(RecursionError) as er:
        unstable_function()

    assert "maximum recursion" in str(er.value)
