x = 10
y = 123


def my_func():
    global x, y

    print("inside 1", x)
    x = 20
    print("inside 1", x)


my_func()
print("outside ", x)
