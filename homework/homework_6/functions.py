
def simple():
    return


simple()


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


with_required_params(1, 2)
with_required_params(1, b=2)
with_required_params(b=1, a=2)


# unpacking parameters as positional or named
args = (3, 4)
with_required_params(*args)  # positional unpacking

kwargs = {"b": 1, "a": 2}
with_required_params(**kwargs)  # named unpacking

args = (3, )
kwargs = {"b": 1}
with_required_params(*args, **kwargs)  # unpacking
with_required_params(2, **kwargs)  # unpacking
with_required_params(*args, b=32)  # unpacking

# you can unpack even empty collections
args = ()
kwargs = {}
with_required_params(*args, *args, **kwargs, **kwargs, a=1, b=2)  # unpacking


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


with_optional_parameters(1)
with_optional_parameters(a="23")
with_optional_parameters(1, "2")
with_optional_parameters(1, b="23")
with_optional_parameters(a="23", b="some")


# never use mutable as default as it is linked to function and can provide unexpected results
def optional_with_mutable_default(data=[]):
    data.append(1)
    return data


a = [1, 2, 3]
optional_with_mutable_default(a)
optional_with_mutable_default(a)
optional_with_mutable_default()
optional_with_mutable_default()
optional_with_mutable_default(a)
optional_with_mutable_default()
optional_with_mutable_default.__defaults__[0]
optional_with_mutable_default()
optional_with_mutable_default.__defaults__[0]


# unlimited positional parameters
def unlimited_positional(a, *args, some="val"):
    """
    Receives 1 required parameter,
    Unlimited amount of positional parameters
    Ana 1 optional named parameter
    """
    return a, args, some


unlimited_positional(1)
unlimited_positional(1, 2, 3, 4, 5, 6)
unlimited_positional(some="123", a=456)
unlimited_positional(1, 2, 3, some="val")


# unlimited named parameters
def unlimited_named(a, some="val", **kwargs):
    """
    Receives 1 required parameter,
    1 optional named parameter
    And unlimited amount of named parameters
    """
    return a, some, kwargs


unlimited_named(1)
unlimited_named(a=1)
unlimited_named(1, val1=3, val2=4)
unlimited_named(some="123", a=456)
unlimited_named(1, some="val")
unlimited_named(1, param1="ad", some="val", param3="any")


def named_only(a, *, b, c=123):
    """
    Receives 2 required parameters, where 2nd is named only parameter,
    And one optional named only parameter
    """
    return a, b, c


named_only(1, b=2)
named_only(1, b=2, c=3)
named_only(b=2, a=1, c=3)


def positional_only(a, /, b, c=123):
    """
    Receives 2 required parameters, where 1st is positional only parameter,
    And one optional parameter
    """
    return a, b, c


positional_only(1, 2)
positional_only(1, 2, 3)
positional_only(1, b=2)
positional_only(1, 2, c=3)
positional_only(1, b=2, c=3)


def positional_only_2(a=1, /, b=2):
    """
    Receives 2 optional parameters, where 1st is positional only parameter
    """
    return a, b


positional_only_2()
positional_only_2(1)
positional_only_2(1, 2)
positional_only_2(1, b=2)
