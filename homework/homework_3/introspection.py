# objects
some_bool = bool()
some_int = int()
some_float = float()
some_str = str()
some_tuple = tuple()
some_list = list()
some_range = range(10)
some_set = set()
some_dict = dict()

some_lambda = lambda: 1


def some_func():
    return 1


def some_gen_func():
    yield 1
    yield 2
    yield 3


class SomeClass:
    """
    my great docstring
    """

    class_atr = 123

    def __init__(self):
        self.instance_attr = 987

    def __call__(self, *args, **kwargs):
        print('Calable')


some_object = SomeClass()


try:
    5 / 0
except ZeroDivisionError as error:
    some_error = error


# type
type(some_bool)
type(some_int)
type(some_float)
type(some_str)
type(some_tuple)
type(some_list)
type(some_range)
type(some_set)
type(some_dict)
type(some_lambda)
type(some_gen_func)
type(some_func)
type(some_object)
type(some_error)

# get type
type(some_bool) is bool
type(some_bool) is int
type(some_bool) is str
type(some_bool) in (str, bool)

# more correct type checks
isinstance(some_bool, bool)
isinstance(some_bool, int)
isinstance(some_bool, float)
isinstance(some_bool, (int, float, str))
isinstance(some_error, ZeroDivisionError)
isinstance(some_error, Exception)

isinstance(some_bool, object)  # is an object
isinstance(some_bool, type)  # but not a type
isinstance(bool, type)   # is a type
isinstance(bool, object)  # but still an object

# subclass
issubclass(bool, bool)
issubclass(bool, int)
issubclass(bool, float)
issubclass(ZeroDivisionError, ArithmeticError)
issubclass(ZeroDivisionError, Exception)


# len
len(some_str)
len(some_dict)
len(some_list)
len(some_tuple)
len(some_set)
len(some_range)

# callable
callable(some_bool)
callable(bool)
callable(some_func)
callable(some_gen_func)
callable(some_lambda)
callable(SomeClass)
callable(some_object)


a = (1, 2, 3)
b = (1, 2, 3)
a == b
a is b
hash(a) == hash(b)
id(a) == id(b)


dir(list)
vars(some_object)
vars(SomeClass)
help(some_object)
some_object.__doc__

# has attr
hasattr(some_list, "append")
hasattr(some_object, "instance_attr")
hasattr(some_object, "class_atr")
hasattr(SomeClass, "class_atr")
hasattr(SomeClass, "instance_attr")

# representation
str("123")
str(123)
repr("123")
repr(123)
