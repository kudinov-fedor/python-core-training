#########################
# conversion to Boolean #
#########################

bool(None)
bool(False)
bool(0)
bool(0.0)
bool("")
bool([])
bool(())
bool({})
bool(set())
bool(bool())
bool(int())
bool(float())
bool(str())
bool(list())
bool(tuple())
bool(dict())

bool(True)
bool(3)
bool(-0.1)

# containers bool check
bool("abc")
bool([False, ])
bool((None, ))
bool({"a": 123})
bool({1, "abc"})
# same as
len("abc") > 0
len([False, ]) > 0
len((None, )) > 0
len({"a": 123}) > 0
len({1, "abc"}) > 0


not 5
not 0
not True
not False
not []
not (1, 2, 3)


# comparison
"it is true" if True else "it is false"
"it is true" if False else "it is false"
"it is true" if "" else "it is false"
"it is true" if "abc" else "it is false"
"it is true" if 0 else "it is false"
"it is true" if 1 else "it is false"
"it is true" if [] else "it is false"
"it is true" if [None] else "it is false"


# take first True item, or last
True or False
False or True
1 or 3
[] or "abc"
None or "some"
None or 0 or "" or [] or "at last some value"
None or 0 or "" or [] or {}

# take first False item, or last
True and False
False and True
1 and 3
[1, 2, 3] and "abc"
"some" and {}
1 and "abc" and 0.0 and "some value"

# priority is important
"" or "Some" and {}
"" or "Some" and {}
False or "" and 123
False or "" and 123


# if all are true
all(["a", 0, True, (1, 2, 3)])
all(["a", -1, True, (1, 2, 3)])
all(["a", -1, False, (1, 2, 3)])
all(["a", -1, True, ()])

# if at least 1 is true
any(["", 0, False, (), None])
any(["", 1, False, (), None])
any(["", 0, True, (), None])
any(["", 0, False, (1,), None])


# filter by default leaves only true elements,
# but you can specify other logic

data = ["cat", "dog", "", None, False, 0, 1, -2, True]
list(filter(None, data))
list(filter(lambda i: isinstance(i, str), data))

