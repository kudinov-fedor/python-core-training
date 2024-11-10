import time


class Timer:

    def __init__(self):
        self.total = 0

    def __enter__(self):
        self.total = 0
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.total += (time.time() - self.start)
