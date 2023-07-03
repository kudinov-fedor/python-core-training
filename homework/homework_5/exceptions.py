

def error_func():
    5 / 0


def error_func_2():
    a = []
    a[0]


def error_func_3():
    x


def error_func_4():
    import invalid


def error_func_5():
    1 + "123"


def error_func_6():
    a = []
    a.invalid


def error_func_7():
    a = lambda: 123
    a(1, 2, 3)


def error_func_8():
    a = lambda i: i
    a()


# traceback several levels deep
def func_1():
    5 / 0


def func_2():
    func_1()


def func_3():
    func_2()


def main_func():
    func_3()
