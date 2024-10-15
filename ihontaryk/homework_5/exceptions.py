# division by zero
def error_func():
    5 / 0


# list index out of range
def error_func_2():
    a = []
    a[0]


# name 'x' is not defined
def error_func_3():
    x


# No module named 'invalid'
def error_func_4():
    import invalid


# unsupported operand type(s) for +: 'int' and 'str'
def error_func_5():
    1 + "123"


# AttributeError
def error_func_6():
    a = []
    a.invalid


# error_func_7.<locals>.<lambda>() takes 0 positional arguments but 3 were given
def error_func_7():
    a = lambda: 123
    a(1, 2, 3)


# error_func_8.<locals>.<lambda>() missing 1 required positional argument: 'i'
def error_func_8():
    a = lambda i: i
    a()


# invalid syntax (<string>, line 1)
def error_func_9():
    eval("x = ")


# maximum recursion depth exceeded
def error_func_10():
    error_func_10()


# traceback several levels deep
def func_1():
    5 / 0


# division by zero
def func_2():
    func_1()


# division by zero
def func_3():
    func_2()


# division by zero
def main_func():
    func_3()


try:
    error_func_10()
except Exception as e:
    print(e)
    print(type(e))
