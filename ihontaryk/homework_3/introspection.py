# Verify in Pyton console the objects creation
some_bool = bool()  # some_bool False
some_int = int()  # some_int 0
some_float = float()  # some_float 0.0
some_str = str()  # some_str ''
some_tuple = tuple()  # some_tuple ()
some_list = list()  # some_list []
some_range = range(10)  # some_range range(0, 10)
some_set = set()  # some_set set()
some_dict = dict()  # some_dict {}

some_lambda = lambda: 1  # some_lambda <function <lambda> at 0x00000265C509A0C0>


def some_func():
    return object


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


some_object = SomeClass()

try:
    5 / 0
except ZeroDivisionError as error:
    some_error = error

# type
type(some_bool)  # <class 'bool'>
type(some_int)  # <class 'int'>
type(some_float)  # <class 'float'>
type(some_str)  # <class 'str'>
type(some_tuple)  # <class 'tuple'>
type(some_list)  # <class 'list'>
type(some_range)  # <class 'range'>
type(some_set)  # <class 'set'>
type(some_dict)  # <class 'dict'>
type(some_lambda)  # <class 'function'>
type(some_gen_func)  # <class 'function'>
type(some_func)  # <class 'function'>
type(some_object)  # <class '__main__.SomeClass'>
type(some_error)  # <class 'ZeroDivisionError'>

# get type
type(some_bool) is bool
type(some_bool) is str
type(some_bool) in (str, bool)

# more correct type checks
isinstance(some_bool, bool) # True
isinstance(some_bool, (int, float, str)) # True
isinstance(some_error, ZeroDivisionError) # True
isinstance(some_error, Exception) # True

isinstance(some_bool, object)  # True
isinstance(some_bool, type)  # False
isinstance(bool, type)  # True
isinstance(bool, object)  # True

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
