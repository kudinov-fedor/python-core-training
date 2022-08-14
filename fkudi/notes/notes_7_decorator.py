def replacer(f):

    def inner():
        print("other print before")
        f()
        print("other print after")

    return inner



def my_func():
    print("my_func")



my_func()
print(my_func.__name__)


my_func = replacer(my_func)

my_func()
print(my_func.__name__)



@replacer     # same as               my_func_2 = replacer(my_func_2
def my_func_2():
    print("my_func")

# my_func_2 = replacer(my_func_2)


my_func_2()



def replacer(f):

    def inner(*args, **kwargs):
        print("other print before")

        res = f(*args, **kwargs)

        print("other print after")

        return res

    return inner
