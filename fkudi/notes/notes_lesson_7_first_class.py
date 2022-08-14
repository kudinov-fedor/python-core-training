
# call with function
def my_func(item: callable, param1):
    print(item)
    print(type(item))
    print(callable(item))

    res = item(param1)
    print(res)  # call
    return res


my_func(list, "123")


def my_func_2(item: callable):
    print(item)
    print(type(item))
    print(callable(item))
    return tuple


res = my_func_2(str)
print(res)
print(repr(res([1, 2, 3, 432])))


# first class functions
sorted
max
min

filter


def item_processor(item):
    ...


x = ["orange", "kiwi", "banana"]
#       6         4        6
# sorted    4,    6,    6

#              6, orange          4 kiwi         6, banana
# sorted       4 kiwi            (6, banana)     (6, orange)

print(sorted(x, reverse=True))  # alphabetical ascending order    "a" "c"     ord("a"), ord("c")


def f(item):
    return len(item)


print(sorted(x, key=f))


def f(item):
    return len(item), item


print(sorted(x, key=f))



some_collection = ["", 1, 2, None, 4, 2, 1, 0, 1, 32, "gdged"]


print(list(filter(None, some_collection)))


def process(item):
    return bool(item)   # true, false


print(list(filter(process, some_collection)))


def process(item):
    return isinstance(item, int)


print(list(filter(process, some_collection)))


f = lambda item: isinstance(item, int)
print(list(filter(f, some_collection)))


print(list(filter(lambda item: isinstance(item, int), some_collection)))


print([item for item in some_collection
       if isinstance(item, int)])
