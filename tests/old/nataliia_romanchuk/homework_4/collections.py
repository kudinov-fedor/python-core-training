
some_str = "abcd"
some_tuple = "a", "b", "c", "d"
some_list = ["a", "b", "c", "d"]
some_set = {"a", "b", "c", "d"}
some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}


# len
len(some_str)
len(some_tuple)
len(some_list)
len(some_set)
len(some_dict)

# contains
"a" in some_str
"a" in some_tuple
"a" in some_list
"a" in some_set
"a" in some_dict

# getitem
some_str[0]  # by index
some_tuple[0]   # by index
some_list[0]  # by index
some_dict["a"]    # by key

# last item
some_str[-1]
some_tuple[-1]
some_list[-1]

# modify
a = [1, 2, 3, 4]
a[3] = "abc"
del a[1]

b = {"a": 123, "b": 456}
b["c"] = 7889
b["b"] = "some"
del b["a"]

# unpack / iterate
list(some_str)
list(some_tuple)
list(some_list)
list(some_set)
list(some_dict)

tuple(some_str)
tuple(some_tuple)
tuple(some_list)
tuple(some_set)
tuple(some_dict)


# multiple assignment
a, b, c, d = some_str
a, b, c, d = some_tuple
a, b, c, d = some_list
a, b, c, d = some_set
a, b, c, d = some_dict

a, *tail = some_str
a, *tail = some_tuple
a, *tail = some_list
a, *tail = some_set
a, *tail = some_dict

*head, d = some_str
*head, d = some_tuple
*head, d = some_list
*head, d = some_set
*head, d = some_dict

*head, d = some_str
*head, d = some_tuple
*head, d = some_list
*head, d = some_set
*head, d = some_dict

a, *middle, d = some_str
a, *middle, d = some_tuple
a, *middle, d = some_list
a, *middle, d = some_set
a, *middle, d = some_dict

a, b, c, d, *tail = some_str
a, b, c, d, *tail = some_tuple
a, b, c, d, *tail = some_list
a, b, c, d, *tail = some_set
a, b, c, d, *tail = some_dict


# iterate protocol
some_str_iter = iter(some_str)
next(some_str_iter)  # get 1 item from iterator
list(some_str_iter)  # get all rest items from iterator
list(some_str_iter)  # iterator exhausted, no items are returned

some_tuple_iter = iter(some_tuple)
next(some_tuple_iter)
list(some_tuple_iter)
list(some_tuple_iter)

some_list_iter = iter(some_list)
next(some_list_iter)
list(some_list_iter)
list(some_list_iter)

some_set_iter = iter(some_set)
next(some_set_iter)
list(some_set_iter)
list(some_set_iter)

some_dict_iter = iter(some_dict)
next(some_dict_iter)
list(some_dict_iter)
list(some_dict_iter)


# sort data (same for min max)
data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]

# sort by age
sorted(data, key=lambda i: i["age"])
sorted(data, key=lambda i: i["age"], reverse=True)

# sort by sex, where F is 0, M is 1 (F goes first - ascending by default)
sorted(data, key=lambda i: i["sex"] == "M")
sorted(data, key=lambda i: i["sex"] == "M", reverse=True)

# sort by sex (F first) and age (asc)
sorted(data, key=lambda i: (i["sex"] == "M", i["age"]))
# sort by sex (F first) and age (desc)
sorted(data, key=lambda i: (i["sex"] == "M", -i["age"]))
# sort by name  alphabetically
sorted(data, key=lambda i: i["name"])


# zip, enumerate, reversed, map, filter
list(filter(lambda i: i == "M", data))
list(enumerate(data))
list(reversed(data))
list(map(lambda i: i["name"], data))

list(zip(data, [1, 2, 3, 4, 5, 6, 7]))
list(zip(data, [1, 2]))
list(zip(data, [1, 2, 3]))
