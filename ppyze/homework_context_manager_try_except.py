class Catcher:
    def __init__(self, *args):
        self.exceptions = args or Exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.exceptions)


if __name__ == "__main__":

    with Catcher():
        5 / 0

    with Catcher(ZeroDivisionError):
        5 / 0

    with Catcher(TypeError, ZeroDivisionError):
        5 / 0

