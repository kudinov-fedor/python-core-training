class CallCounts:
    calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"{__class__.__name__} was called {self.calls} times.")


if __name__ == '__main__':
    caller = CallCounts()
    assert caller.calls == 0
    caller()
    caller()
    caller()
    assert caller.calls == 3
