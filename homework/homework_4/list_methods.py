some_str = "fabcdefdgab"
some_list = [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
some_tuple = (1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4)


some_tuple.index(2)
some_list.index(2)
some_str.index("d")
some_str.index("ab")

some_tuple.count(3)
some_list.count(3)
some_str.count("a")
some_str.count("ab")


# Methods Specific Only for List

# copy()      Returns a shallow copy of the list
data = some_list.copy()
data == some_list
data is some_list

# Next Methods change List

# append()    Adds an element at the end of the list
data = some_list.copy()
data.append(100)
data == some_list

# insert()    Adds an element at the specified position
data = some_list.copy()
data.insert(0, "a")   # insert in front
data == some_list

data = some_list.copy()
data.insert(-1, "a")  # insert before last
data == some_list

# clear()     Removes all the elements from the list
data = some_list.copy()
data.clear()
data == some_list

# extend()    Add the elements of a list (or any iterable), to the end of the current list
data = some_list.copy()
data.extend([100, 200, 300])
data == some_list

data = some_list.copy()
data.extend("abc")
data == some_list

data = some_list.copy()
data.extend({"a": 123, "b": 456})
data == some_list

# pop()       Removes and returns the element at the specified position
data = some_list.copy()
popped_item = data.pop()  # pop last
data == some_list

data = some_list.copy()
popped_item = data.pop(0)   # pop first
data == some_list

# remove()    Removes the item with the specified value
data = some_list.copy()
data.remove(5)  # remove first occurrence
data == some_list

# reverse()   Reverses the order of items in the list
data = some_list.copy()
data.reverse()
data == some_list

# sort()      Sort items in a list in ascending order
data = some_list.copy()
data.sort()
data == some_list

data.sort(reverse=True)
data == some_list
