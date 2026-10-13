# operations
"cat" < "dog"
("c", "a", "t") < ("d", "o", "g")
["c", "a", "t"] < ["d", "o", "g"]

"cat" + "dog"
("c", "a", "t") + ("d", "o", "g")
["c", "a", "t"] + ["d", "o", "g"]

"cat" * 3
("c", "a", "t") * 3
["c", "a", "t"] * 3


# inplace operations
a = "Hello"
b = a
a += " World"
a == b
a is b

a = [1, 2, 3]
b = a
a += [4, 5, 6]
a == b
a is b

a = (1, 2, 3)
b = a
a += (4, 5, 6)
a == b
a is b


# get slices
"cat"[:2]
("c", "a", "t")[:2]
["c", "a", "t"][:2]
range(3)[:2]

[1, 2, 3, 4, 5, 6, 7, 8, 9][:]
[1, 2, 3, 4, 5, 6, 7, 8, 9][:5]
[1, 2, 3, 4, 5, 6, 7, 8, 9][2:5]
[1, 2, 3, 4, 5, 6, 7, 8, 9][-4:]
[1, 2, 3, 4, 5, 6, 7, 8, 9][::2]
[1, 2, 3, 4, 5, 6, 7, 8, 9][::-1]

[1, 2, 3, 4, 5, 6, 7, 8, 9][None:None]
[1, 2, 3, 4, 5, 6, 7, 8, 9][None:None:None]

start, end, step = None, None, None
[1, 2, 3, 4, 5, 6, 7, 8, 9][start:end:step]

start, end, step = None, 7, 2
[1, 2, 3, 4, 5, 6, 7, 8, 9][start:end:step]

my_slice = slice(None, 7, 2)
[1, 2, 3, 4, 5, 6, 7, 8, 9][my_slice]


# modify using slice
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[4:4] = ["abc", "def"]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[4:7] = ["abc", "def"]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del data[4:7]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[:] = []

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[0:0] = ["abc"]
