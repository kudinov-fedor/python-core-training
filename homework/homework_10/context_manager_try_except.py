
class Catcher:

    def __init__(self, *exceptions):
        ...

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


if __name__ == "__main__":

    with Catcher():
        5 / 0

    with Catcher(ZeroDivisionError):
        5 / 0

    with Catcher(TypeError, ZeroDivisionError):
        5 / 0
