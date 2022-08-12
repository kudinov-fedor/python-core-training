x = 111   # global scope
y = []


def func_1():
    global x

    print("in func 1", x)
    x = 123                # global
    print("in func 2", x)

    print("in func 1", y)

    y.append(12)
    print("in func 2", y)

    some_print_func()


# error
try:
    func_1()
except NameError as e:
    print(e)


def some_print_func():
    print("hi here")


print("out of func", y)

func_1()
print("out of func", x)
print("out of func", y)

func_1()
func_1()
print("out of func", y)  # [12, 12, 12]


# Functional Programming
# simple func
# no side effect
# in ->  func  -> out
# 1 return - in the end
# does not interract with global  - not True
# immutable objects

# KISS - keep it simple and stupid
