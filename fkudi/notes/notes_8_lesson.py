
class MyGreatClass:
    y = "abc"



item1 = MyGreatClass()
item2 = MyGreatClass()


print(type(item1))
assert type(item1) is MyGreatClass
assert type(item2) is MyGreatClass


item1.x = 123
item2.x = 321


print(item1.x)
print(item1.y)
print(item2.x)
print(item2.y)

print(vars(item1))



MyGreatClass.y = "cdef"
print(item1.y)
print(item2.y)

item2.y = "my own y"

print(item1.y)
print(item2.y)
print(vars(item1))
print(vars(item2))

print(vars(MyGreatClass))

del item2.y
print(item2.y)


# del MyGreatClass.y
# print(item2.y)

print(item1)
print(item2)


print(id(item1), id(item2))


# class attrs            level1
# object attributes       level2


# item1()   # not callable
# list(item1)  # not iterable

# with item1:   # object is not a context manager
#     ...

#  item1[0]

# item1 < item2    not comparable

item1 == item2       # id(item1) == id(item2)


print(str(item1))
print(repr(item1))
print(format(item1))

# len(item1)      # len is not defined


a = {item1: "bla bla bla"}  # by default object can be used as key
print(a[item1])
