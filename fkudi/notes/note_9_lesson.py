


x = [1, 2, {"a": 321}]


# y = x.copy()
#
#
# print(x)
# print(y)
#
# print(x is y)
#
# print(id(x[2]))
# print(id(y[2]))
#
# x[2]["asdf"] = 123124
# print(x)
# print(y)


from copy import deepcopy


y = deepcopy(x)

print(x)
print(y)

print(x is y)

print(id(x[2]))
print(id(y[2]))

x[2]["asdf"] = 123124
print(x)
print(y)



