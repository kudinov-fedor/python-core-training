class Counter:
    def __init__(self):
        self.state = 0

    def __call__(self):
        self.state += 1
        return self.state


if __name__ == '__main__':
    c = Counter()
    assert c() == 1
    assert c() == 2
