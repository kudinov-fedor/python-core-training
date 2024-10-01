# Verify in Python Console introspection of objects

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
issubclass(bool, bool) # True
issubclass(bool, int) # True
issubclass(bool, str) # False
issubclass(bool, float) # False
issubclass(ZeroDivisionError, ArithmeticError) # True
issubclass(ZeroDivisionError, Exception) # True

# len
len(some_str) # 0
len(some_dict) # 0
len(some_list) # 0
len(some_tuple)  # 0
len(some_set) # 0
len(some_range) # 10

# callable
callable(some_bool) # False
callable(bool) # True
callable(some_func) # True
callable(some_gen_func) # True
callable(some_lambda)  # True
callable(SomeClass) #True
callable(some_object) # False

a = (1, 2, 3)
b = (1, 2, 3)
a == b # True
a is b # False
hash(a) # 529344067295497451
hash(a) == hash(b) # True
id(a) # 2367368774976
id(a) == id(b) # False

dir(list) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__',
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
# '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
vars(some_object) # {'instance_attr': 987}
vars(SomeClass) # mappingproxy({'__module__': '__main__', '__doc__': '\n    my great docstring\n    ',
# 'class_atr': 123, '__init__': <function SomeClass.__init__ at 0x00000227322AF380>, '__dict__': <attribute
# '__dict__' of 'SomeClass' objects>, '__weakref__': <attribute '__weakref__' of 'SomeClass' objects>})
help(some_object)
some_object.__doc__ #'\n    my great docstring\n    '

# has attr
hasattr(some_list, "append") # True
hasattr(some_object, "instance_attr") # True
hasattr(some_object, "class_atr") # True
hasattr(SomeClass, "class_atr") # True
hasattr(SomeClass, "instance_attr") # False

# representation
str("123") # '123'
str(123) # '123'
repr("123") # "'123'"
repr(123) # '123'
