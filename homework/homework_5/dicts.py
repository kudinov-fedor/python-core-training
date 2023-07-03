# DICTS
some_dict = {"a": 123, "b": 456, "c": 789}
some_dict_2 = {"c": 789, "a": 123, "b": 456}
some_dict_3 = dict.fromkeys("abc")
wierd_dict = {"a": 1, 2: "b",
              None: "abc",
              (1, "a"): "some",
              True: "kek",
              frozenset((1, 2)): "lol"}

some_dict == some_dict_2

# is container
"a" in some_dict
len(some_dict)
list(some_dict_2)


# methods
some_dict["a"]
some_dict.get("a")
some_dict.get("invalid")
some_dict.get("invalid", "default_val")


some = {"a": 1, "b": 2}
some.update({"b": "b", "c": "c"})
sopy_of_some = some.copy()  # shallow copy
some.clear()
item = some.pop("a")
item = some.pop("invalid", "default_val")

# setdefault - return value for key, but if key not present, create it with default value, and return value
# same as:   item = data.get("k", "val")]; data["k"] = item
item = some.setdefault("a", "default_for_a")
"a" in some
some["a"] == "default_for_a"


item = some.setdefault("a", "other_default_for_a")
"a" in some
some["a"] == "default_for_a"


# dict comprehension
{k: v for k, v in some_dict.items()}
{k * 2: str(v) for k, v in some_dict.items()}
{k: v for k, v in some_dict.items() if k <= "b"}


# index and group
data = [{"age": 16, "second_name": "Parris", "name": "John", "sex": "M"},
        {"age": 34, "second_name": "Atkinson", "name": "Marry", "sex": "F"},
        {"age": 15, "second_name": "Katon", "name": "Marry", "sex": "F"},
        {"age": 25, "second_name": "Maton", "name": "Mathew", "sex": "M"}]


# index by name - 1 value for each key
by_name = {i["name"]: i for i in data}
by_name["John"]
by_name["Marry"]


# index by name, second_name
by_name = {(i["name"], i["second_name"]): i for i in data}
by_name["John", "Parris"]
by_name["Marry", "Katon"]


# group by sex
by_sex = {}
for i in data:
    if i["sex"] not in by_sex:
        by_sex[i["sex"]] = []
    by_sex[i["sex"]].append(i)

len(by_sex["M"])
len(by_sex["F"])


# other option - setdefault:
# if key is not present, it will be created with default, and returned
by_sex = {}
for i in data:
    by_sex.setdefault(i["sex"], []).append(i)

len(by_sex["M"])
len(by_sex["F"])


# Other option - use default dict
from collections import defaultdict

by_sex = defaultdict(list)  # if key is not present, it will be created with value = list()
for i in data:
    by_sex[i["sex"]].append(i)

len(by_sex["M"])
len(by_sex["F"])
