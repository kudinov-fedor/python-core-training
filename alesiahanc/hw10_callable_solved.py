class SimpleCallable:

    def __init__(self):
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        """
        Increases call_count attribute every time the class object is called
        """
        self.call_count += 1


if __name__ == "__main__":

    a = SimpleCallable()

    assert a.call_count == 0

    a()
    a()
    assert a.call_count == 2