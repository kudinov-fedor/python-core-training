# list
a = [1, 2, 3]
b = a

id(a)
id(b)
a is b
a == b

a += [4]
id(a)
id(b)
a is b
a == b


# str
a = "123"
b = a

id(a)
id(b)
a is b
a == b

a += "4"
id(a)
id(b)
a is b
a == b

# tuple
a = (1, 2, 3)
b = a

id(a)
id(b)
a is b
a == b


a += (4,)

id(a)
id(b)
a is b
a == b
