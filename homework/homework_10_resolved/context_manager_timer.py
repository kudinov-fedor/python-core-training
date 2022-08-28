import time


class Timer:
    def __init__(self):
        self.total = 0
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert self.start, "Timer never started"
        self.total += (time.time() - self.start)


if __name__ == "__main__":

    with Timer() as timer:
        time.sleep(3)

    assert timer.total >= 3
    print(timer.total)

    with timer:
        time.sleep(2)

    assert timer.total >= 2
    print(timer.total)
