None
True
False


10
-2
0


5.2
-3.4
0.0


"abc"

'abc'

"""abc"""

'''abc'''

("abc"
"def")

"abc\ndef"

"""abc
def"""


()
12,5
(12)
(12,)


[]
[12]
[12,]
["abc", 12.4, (), None, True]


{}
{"abc": 123}

{}
{1, 2, 3}

# ========================

bool
int
float
str
list
dict
set

bool()
int()
float()
str()
list()
dict()
set()


str.join
"".join

id(str.join)
id("".join)

str.join("|", "abc")
"|".join("abc")

str.join("|", ["a", "b", "c"])
"|".join(["a", "b", "c"])


# --------------------------

"Hello World".split(" ")[0]

a = "Hello World"
b = a.split
c = " "
d = b(c)
e = 0
f = d[e]
