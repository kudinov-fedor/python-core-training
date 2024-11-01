# operations
"cat" < "dog" # True
("c", "a", "t") < ("d", "o", "g") # True
["c", "a", "t"] < ["d", "o", "g"] # True

"cat" + "dog" # 'catdog'
("c", "a", "t") + ("d", "o", "g") # ('c', 'a', 't', 'd', 'o', 'g')
["c", "a", "t"] + ["d", "o", "g"] # ['c', 'a', 't', 'd', 'o', 'g']

"cat" * 3 # 'catcatcat'
("c", "a", "t") * 3 # ('c', 'a', 't', 'c', 'a', 't', 'c', 'a', 't')
["c", "a", "t"] * 3 # ['c', 'a', 't', 'c', 'a', 't', 'c', 'a', 't']


# inplace operations
a = "Hello" # 'Hello'
b = a # 'Hello'
a += " World" # 'Hello World'
a == b # False
a is b # False

a = [1, 2, 3] # [1, 2, 3]
b = a # [1, 2, 3]
a += [4, 5, 6] # [1, 2, 3, 4, 5, 6]
a == b # True
a is b # True

a = (1, 2, 3) # (1, 2, 3)
b = a # (1, 2, 3)
a += (4, 5, 6) # (1, 2, 3, 4, 5, 6)
a == b # False
a is b # False


# get slices
"cat"[:2] # 'ca'
("c", "a", "t")[:2] # ('c', 'a')
["c", "a", "t"][:2] # ['c', 'a']
range(3)[:2] # range(0, 2)

[1, 2, 3, 4, 5, 6, 7, 8, 9][:] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9][:5] # [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6, 7, 8, 9][2:5] # [3, 4, 5]
[1, 2, 3, 4, 5, 6, 7, 8, 9][-4:] # [6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9][::2] # [1, 3, 5, 7, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9][::-1] # [9, 8, 7, 6, 5, 4, 3, 2, 1]

[1, 2, 3, 4, 5, 6, 7, 8, 9][None:None] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9][None:None:None] # [1, 2, 3, 4, 5, 6, 7, 8, 9]

start, end, step = None, None, None
[1, 2, 3, 4, 5, 6, 7, 8, 9][start:end:step] #[1, 2, 3, 4, 5, 6, 7, 8, 9]

start, end, step = None, 7, 2
[1, 2, 3, 4, 5, 6, 7, 8, 9][start:end:step] # [1, 3, 5, 7]

my_slice = slice(None, 7, 2)
[1, 2, 3, 4, 5, 6, 7, 8, 9][my_slice]


# modify using slice
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[4:4] = ["abc", "def"] # data: [1, 2, 3, 4, 'abc', 'def', 5, 6, 7, 8, 9]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[4:7] = ["abc", "def"] # [1, 2, 3, 4, 'abc', 'def', 8, 9]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del data[4:7] # [1, 2, 3, 4, 8, 9]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[:] = [] # []

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data[0:0] = ["abc"] # ['abc', 1, 2, 3, 4, 5, 6, 7, 8, 9]


def check_palindrome_words(word) -> bool:
    return word == word[::-1]

if __name__ == '__main__':
    print(check_palindrome_words('level'))
