# SETS

some_set = {"a", "b", "c"}
some_set_2 = {"b", "a", "c"}

# is container
len(some_set)  # 3
"a" in some_set  # True
list(some_set)  # ['b', 'a', 'c']

# is subset/superset
some_set == some_set_2  # True
some_set <= some_set_2  # True
some_set_2 <= some_set  # True

{"a"} < some_set  # True
{"f"} < some_set  # False
{"a", "c"} < some_set  # True
some_set > {"a", "c"}  # True

{"a", "c"}.issubset({"a", "c", "b"})  # True
{"a", "c"}.issubset(["a", "b", "c"])  # True
{"a", "c"}.issubset("cab")  # True
some_set.issuperset({"a", "c"})  # True
some_set.issuperset(["a", "c"])  # True
some_set.issuperset(["ac"])  # False

# union
{"a", "b", "x"} | {"a", "x", "f"}  # {'b', 'f', 'x', 'a'}
{"a", "b", "x"}.union({"a", "x", "f"})  # {'b', 'f', 'x', 'a'}

# update
a = {"a", "b", "c"}
a |= {"b", "x", "d"}  # {'d', 'b', 'c', 'x', 'a'}
a.update({"f", "x", "k"})  # {'d', 'b', 'k', 'c', 'x', 'f', 'a'}
a.update("safz")  # {'d', 'c', 'a', 'b', 'k', 'z', 'f', 's', 'x'}
a.update(["r", "e" "z"])  # {'d', 'c', 'a', 'r', 'b', 'k', 'z', 'f', 'ez', 's', 'x'}

# diff
{"a", "b", "x"} - {"a", "x", "f"}  # {'b'}
{"a", "b", "x"}.difference({"a", "x", "f"})  # {'b'}

# symetric diff
{"a", "b", "x"} ^ {"a", "x", "f"}  # {'b', 'f'}
{"a", "b", "x"}.symmetric_difference({"a", "x", "f"})  # {'b', 'f'}

# intersection
{"a", "b", "x"} & {"a", "x", "f"}  # {'a', 'x'}
{"a", "b", "x"}.intersection({"a", "x", "f"})  # {'a', 'x'}


def remove_min_max_loop(any_set: set, number: int) -> set:
    if number <= 0 or number > (len(any_set) // 2):
        raise ValueError

    for i in range(number):
        any_set.remove(max(any_set))
        any_set.remove(min(any_set))

    return any_set


set4 = {'a', 'b', 'c', 'd', 'd'}

try:
    remove_min_max_loop(set4, 8)
except ValueError as e1:
    print(type(e1))
except TypeError as e2:
    print(type(e2))
finally:
    print('Function remove_min_max_loop was executed')
