import random

import pytest

from obalk.home_task_7.retying import unstable_function


def test_make_stable(monkeypatch):
    monkeypatch.setattr(random, 'random', 0.1)
    with pytest.raises(ValueError) as er:
        unstable_function()

    assert "unstable_function did not retry in attempts=3" in str(er.value)
