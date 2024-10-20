import random


def retry(func):
    """
    Decorator which will retry inner function if it failed
    """

    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                continue

    return wrapper


@retry
def positive_function(a, b):
    result = random.randint(a, b)

    if result < 0:
        raise ValueError(result, "Failed because result is negative")
    return result


if __name__ == "__main__":
    print(positive_function(a=-10, b=10))
