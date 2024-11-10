
class SimpleCallable:

    call_count = 0

    def __call__(self):
        self.call_count += 1
