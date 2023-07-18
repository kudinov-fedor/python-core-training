"""
Create decorator, which will retry inner function multiple times until it passes
"""
import random


def parametrised_decorator(max_retries=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 1
            while True:
                try:
                    res = func(*args, **kwargs)
                    print(f'Retry No.{retries}')
                    return res
                except Exception as error:
                    if retries == max_retries:
                        print(f'Retry No.{retries}')
                        print(f'{error}: Maximum of retries has been reached')
                        break
                    else:
                        print(f'Retry No.{retries}')
                        retries += 1
        return wrapper
    return decorator


@parametrised_decorator(max_retries=3)
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


if __name__ == '__main__':
    print(unstable_function())
