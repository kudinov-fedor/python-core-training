
class SimpleCallable:
    ...


if __name__ == "__main__":

    a = SimpleCallable()

    assert a.call_count == 0

    a()
    a()
    assert a.call_count == 2
