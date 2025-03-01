def my_simple_function_with_required_params(num1: int, num2: float) -> float:
    res = num1 * num2
    return res


def with_optional_parameters(a, b="hi"):
    return a, b


def unlimited_positional(a, *args, some="val"):
    """
    Receives 1 required parameter,
    Unlimited amount of positional parameters
    Ana 1 optional named parameter
    """
    return a, args, some


def unlimited_named(a, some="val", **kwargs):
    """
    Receives 1 required parameter,
    1 optional named parameter
    And unlimited amount of named parameters
    """
    return a, some, kwargs
