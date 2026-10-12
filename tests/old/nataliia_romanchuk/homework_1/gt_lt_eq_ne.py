1 < 2
5 >= 3.5
"a" < "b"
"dog" > "day"
(1, 2) > (1, 3)
("d", "o", "g") > ("d", "a", "y")
["d", "o", "g"] <= ["d", "a", "y"]
True > False
True == 1
False == 0
1 != 0

# double comparison
1 <= 5 <= 9
# same as   1 <= 5  and 5 <= 9
1 <= 5 > 2

0 <= 5 == True
(0 <= 5) == True
0 <= (5 == True)
0 <= 5 and 5 == True

# equal vs identical
a = []
b = a
c = []

# identity check
a is b
a is not c
# same as
id(a) == id(b)
id(a) != id(c)

# equality check
a == b
a == c


# contains
"a" in ["a", "b", "c"]
"z" not in ["a", "b", "c"]
"a" in "abc"

"z" not in "abc"
"a" in ("a", "b", "c")
"z" not in ("a", "b", "c")

"ab" in "abc"
"ab" in ["a", "b", "c"]


# implicit comparison
max(3, 4, 5)
min([5, 3, 4])
max("sfdsdf")
max([2, 3, 1, -2, -5, -8, 12])
max([2, 3, 1, -2, -5, -8, 12], key=abs)

max("banana", "ball", "cat")
max("banana", "ball", "cat", key=len)
min("banana", "ball", "cat")
min("banana", "ball", "cat", key=len)

# sort
sorted([2, 4, -5, 6, -1])
sorted([2, 4, -5, 6, -1], reverse=True)
sorted([2, 4, -5, 6, -1], reverse=False)
sorted([2, 4, -5, 6, -1], key=abs)

sorted(["banana", "ball", "cat"])
sorted(["banana", "ball", "cat"], key=len)
sorted(["banana", "ball", "cat"], reverse=True)
sorted(["banana", "ball", "cat"], reverse=True, key=len)
