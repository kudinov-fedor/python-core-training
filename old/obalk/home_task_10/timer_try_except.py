import time


class Timer:

    def __init__(self, *exceptions):
        self.total: float = 0.0
        self.exceptions = exceptions or BaseException

    def __enter__(self):
        print("Code timer has started")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.total = time.perf_counter() - self.start
        print(f"Code within 'with' block was executed in {self.total}")
        if not exc_type:
            print("No error occurred")
            return False
        if issubclass(exc_type, self.exceptions):
            print(f"Exception {exc_type} was suppressed")
        else:
            raise exc_type
        return True


if __name__ == '__main__':
    wait_sec = 1
    with Timer(IndexError) as timer:
        time.sleep(wait_sec)

    assert timer.total > wait_sec

    wait_sec = 2
    with timer:
        time.sleep(wait_sec)

    assert timer.total > wait_sec
    assert timer.total < wait_sec + 1

    with Timer(IndexError) as timer:
        time.sleep(wait_sec)
        raise IndexError

    assert timer.total > wait_sec
