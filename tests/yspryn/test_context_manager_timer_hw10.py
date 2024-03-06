import time
from yspryn.hw10.context_manager_timer import Timer


def test_context_manager_timer():
    with Timer() as timer:
        time.sleep(3)

    assert timer.total >= 3
    print(timer.total)

    with timer:
        time.sleep(2)

    assert timer.total >= 2
    print(timer.total)
