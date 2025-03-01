import time

from irepela.homework_10.context_manager_timer import Timer


def test_timer():

    with Timer() as timer:
        time.sleep(3)

    assert timer.total >= 3

    with timer:
        time.sleep(2)

    assert timer.total >= 2
