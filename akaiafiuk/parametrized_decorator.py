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
            for current_try in range(number_of_tries):
                try:
                    res = func(*args, **kwargs)
                    return res
                except ValueError:
                    if current_try == number_of_tries - 1:
                        raise
        return wrapper
    return decorator


@ordinary_decorator
def get_random():
    import random
    x = random.random()
    assert x <= 0.5
    return x


@parametrised_decorator(1)
def get_random_param():
    import random
    x = random.random()
    if x > 0.5:
        raise ValueError("x > 0.5")
    return x
