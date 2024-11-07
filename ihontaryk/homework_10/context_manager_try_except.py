class Catcher:
    def __init__(self, *exceptions):
        self.exceptions = exceptions or Exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            return issubclass(exc_type, self.exceptions)


def divide_numbers(num1, num2):
    return num1/num2


if __name__ == "__main__":
    with Catcher():
        print(divide_numbers(10, 5))

    with Catcher():
        divide_numbers(5, 0)

    with Catcher(ZeroDivisionError):
        divide_numbers(5, 0)

    with Catcher(TypeError, ZeroDivisionError):
        divide_numbers(5, 0)
