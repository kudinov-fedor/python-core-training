import random


def retry_func(func):

    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                print(error)
                continue

    return wrapper


@retry_func
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    result = unstable_function()
    print(result)
