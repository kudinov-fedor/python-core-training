def ordinary_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        while True:
            try:
                res = func(*args, **kwargs)
                return res
            except AssertionError:
                continue
    return wrapper


def parametrised_decorator(number_of_tries):
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            for _ in range(number_of_tries):
                try:
                    res = func(*args, **kwargs)
                    return res
                except AssertionError:
                    continue
            raise BadLuckException(f"Seems that all {number_of_tries} attempts to call {func} had failed")
        return wrapper
    return decorator


class BadLuckException(BaseException):
    ...


@ordinary_decorator
def get_random():
    import random
    x = random.random()
    assert x <= 0.5
    return x


@parametrised_decorator(10)
def get_random_param():
    import random
    x = random.random()
    assert x <= 0.5
    return x
