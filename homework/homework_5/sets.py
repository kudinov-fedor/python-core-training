# SETS

some_set = {"a", "b", "c"}
some_set_2 = {"b", "a", "c"}

# is container
len(some_set)
"a" in some_set
list(some_set)

# is subset/superset
some_set == some_set_2
some_set <= some_set_2
some_set_2 <= some_set

{"a"} < some_set
{"f"} < some_set
{"a", "c"} < some_set
some_set > {"a", "c"}

{"a", "c"}.issubset({"a", "c", "b"})
{"a", "c"}.issubset(["a", "b", "c"])
{"a", "c"}.issubset("cab")
some_set.issuperset({"a", "c"})
some_set.issuperset(["a", "c"])
some_set.issuperset(["ac"])

# union
{"a", "b", "x"} | {"a", "x", "f"}
{"a", "b", "x"}.union({"a", "x", "f"})

# update
a = {"a", "b", "c"}
a |= {"b", "x", "d"}
a.update({"f", "x", "k"})
a.update("safz")
a.update(["r", "e" "z"])

# diff
{"a", "b", "x"} - {"a", "x", "f"}
{"a", "b", "x"}.difference({"a", "x", "f"})

# symetric diff
{"a", "b", "x"} ^ {"a", "x", "f"}
{"a", "b", "x"}.symmetric_difference({"a", "x", "f"})

# intersection
{"a", "b", "x"} & {"a", "x", "f"}
{"a", "b", "x"}.intersection({"a", "x", "f"})
