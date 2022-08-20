import time


class Timer:
    def __init__(self):
        self.total = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


if __name__ == "__main__":

    with Timer() as timer:
        time.sleep(3)

    assert timer.total >= 3
    print(timer.total)

    with timer:
        time.sleep(2)

    assert timer.total >= 2
    print(timer.total)
