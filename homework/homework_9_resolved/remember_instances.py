class MemorisingClass:

    _instances = []

    def __new__(cls, *args, **kwargs):
        item = super().__new__(cls)
        cls._instances.append(item)
        return item


if __name__ == "__main__":
    a = MemorisingClass()
    b = MemorisingClass()
    c = MemorisingClass()

    assert a in MemorisingClass._instances
    assert b in MemorisingClass._instances
    assert c in MemorisingClass._instances

    del a, b, c
    assert len(MemorisingClass._instances) == 3
