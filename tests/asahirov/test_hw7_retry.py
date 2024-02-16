"""
Create decorator, which will retry inner function multiple times untill it passes
"""
import random
import pytest


def retry_decorator(retries: int = 5, exception_types: tuple = (Exception,)):
    def retry(func):
        def wrapper(*args, **kwargs):
            error = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except exception_types as e:
                    error = e
                    print(f"Function failed. Retries count: #{i + 1}: {e}")
            if error:
                raise error
        return wrapper
    return retry


@retry_decorator(retries=10, exception_types=(ValueError,))
def unstable_function():
    res = random.random()
    if res < 0.5:
        raise ValueError("Unpredictable Error")
    return res


def test_unstable_function_success(mocker):
    success_value = 0.51
    mocker.patch('random.random', return_value=success_value)
    assert unstable_function() == success_value


def test_unstable_function_failed(mocker):
    failed_value = 0.49
    mocker.patch('random.random', return_value=failed_value)
    with pytest.raises(ValueError):
        unstable_function()
