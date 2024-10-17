def with_required_params(a, b):
    """
    Function receives 2 required parameters,
    They can be sent as positional or as named parameters when you call a function

    Examples:

    with_required_params(1, 2)  # positional only
    with_required_params(1, b=2)  # mixed
    with_required_params(b=1, a=2)  # named only
    """
    return a, b


def with_optional_parameters(a, b="hi"):
    """
    Function receives 2 parameters: 1 required, and 2nd optional,
    They can be sent as positional or as named parameters when you call a function

    Examples:

    with_optional_parameters(1)
    with_optional_parameters(a="23")
    with_optional_parameters(1, "2")
    with_optional_parameters(1, b="23")
    with_optional_parameters(a="23", b="some")
    """
    return a, b


# unlimited positional parameters
def unlimited_positional(a, *args, some="val"):
    """
    Receives 1 required parameter,
    Unlimited amount of positional parameters
    Ana 1 optional named parameter
    """
    return a, args, some


# unlimited named parameters
def unlimited_named(a, some="val", **kwargs):
    """
    Receives 1 required parameter,
    1 optional named parameter
    And unlimited amount of named parameters
    """
    return a, some, kwargs


def test_with_required_params():
    assert with_required_params(1, 2) == (1, 2)
    assert with_required_params(b=1, a=2) == (2, 1)


def test_unpacking():
    args = (3, 4)
    kwargs = {"b": 1, "a": 2}
    assert with_required_params(*args) == args
    assert with_required_params(**kwargs) == (2, 1)

    args = (3,)
    kwargs = {"b": 1}
    assert with_required_params(*args, b=32) == (3, 32)
    assert with_required_params(2, **kwargs) == (2, 1)
    assert with_required_params(*args, **kwargs) == (3, 1)


def test_with_optional_params():
    assert with_optional_parameters(1) == (1, "hi")
    assert with_optional_parameters(a="23") == ("23", "hi")
    assert with_optional_parameters(1, "2") == (1, "2")
    assert with_optional_parameters(1, b="23") == (1, "23")
    assert with_optional_parameters(a="23", b="some") == ("23", "some")


def test_unlimited_positional():
    assert unlimited_positional(1) == (1, (), "val")
    assert unlimited_positional(1, 2, 3, 4, 5, 6) == (1, (2, 3, 4, 5, 6), "val")
    assert unlimited_positional(some="123", a=456) == (456, (), "123")
    assert unlimited_positional(1, 2, 3, some="val") == (1, (2, 3), "val")


def test_unlimited_named():
    assert unlimited_named(1) == (1, "val", {})
    assert unlimited_named(a=1) == (1, "val", {})
    assert unlimited_named(1, val1=3, val2=4) == (1, "val", {"val1": 3, "val2": 4})
    assert unlimited_named(some="123", a=456) == (456, "123", {})
    assert unlimited_named(1, some="val") == (1, "val", {})
    assert unlimited_named(1, param1="ad", some="val", param3="any") == (1, "val", {"param1": "ad", "param3": "any"})
