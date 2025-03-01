import time


class Timer:

    def __init__(self):
        self.total: float = 0.0

    def __enter__(self):
        print("Code timer has started")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.total = time.perf_counter() - self.start
        print(f"Code within 'with' block was executed in {self.total}")


if __name__ == '__main__':
    wait_sec = 3
    with Timer() as timer:
        time.sleep(wait_sec)

    assert timer.total > wait_sec

    wait_sec = 4
    with timer:
        time.sleep(wait_sec)

    assert timer.total > wait_sec
    assert timer.total < wait_sec + 1
