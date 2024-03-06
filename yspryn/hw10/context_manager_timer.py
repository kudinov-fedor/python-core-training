import time


class Timer:
    def __init__(self):
        self.total = 0

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish_time = time.time()
        self.total = self.finish_time - self.start_time
