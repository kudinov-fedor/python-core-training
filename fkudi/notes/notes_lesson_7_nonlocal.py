
a = 123   # global

def some_func():
    # local scope of some_func
    # non local scope of create_number

    # CLOSURE
    b = 5

    def create_number():   # local scope of some_func
        nonlocal b

        c = "12343"     # local scope of create_number function

        # print("nonlocal b",  b)
        b = b + 1
        # print("nonlocal b",  b)
        return b

    return create_number


x = some_func()
y = some_func()

print(type(x))
print(x)

print(x())
print(x())

del some_func


print(x())
print(x())
print(x())
print(x())

print(y())
print(y())
print(y())


