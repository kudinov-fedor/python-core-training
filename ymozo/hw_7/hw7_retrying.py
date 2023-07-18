import random
import logging


def retry(max_retries=5):
    def retry_func(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while max_retries > retries:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    logging.warning(error)
                    retries += 1
            raise RuntimeError(f"Function {func.__name__} failed after {max_retries} retries")

        return wrapper
    return retry_func


@retry(max_retries=3)
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == "__main__":
    result = unstable_function()
    print(result)
