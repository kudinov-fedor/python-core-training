some_str = "fabcdefdgab" # 'fabcdefdgab'
some_list = [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
# [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
some_tuple = (1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4)
#(1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4)


some_tuple.index(2) # 1
some_list.index(2) # 1
some_str.index("d") # 4
some_str.index("ab") # 1

some_tuple.count(3) # 2
some_list.count(3) # 2
some_str.count("a") # 2
some_str.count("ab") # 2


# Methods Specific Only for List

# copy()      Returns a shallow copy of the list
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data == some_list # True
data is some_list # False

# Next Methods change List

# append()    Adds an element at the end of the list
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.append(100) # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4, 100]
data == some_list  # False

# insert()    Adds an element at the specified position
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.insert(0, "a")
# insert in front ['a', 1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data == some_list # False

data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.insert(-1, "a")
# insert before last [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 'a', 4]
data == some_list # False

# clear()     Removes all the elements from the list
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.clear() # []
data == some_list # False

# extend()    Add the elements of a list (or any iterable), to the end of the current list
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.extend([100, 200, 300])
# [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4, 100, 200, 300]
data == some_list # False

data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.extend("abc") # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4, 'a', 'b', 'c']
data == some_list # False

data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.extend({"a": 123, "b": 456})
# [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4, 'a', 'b']
data == some_list # False

# pop()       Removes and returns the element at the specified position
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
popped_item = data.pop()
# pop last [1, 2, 3, 4, 5, 6, 1, 3, 2, 5]
data == some_list # False

data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
popped_item = data.pop(0)
# pop first [2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data == some_list # False

# remove()    Removes the item with the specified value
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.remove(5)
# remove first occurrence [1, 2, 3, 4, 6, 1, 3, 2, 5, 4]
data == some_list # False

# reverse()   Reverses the order of items in the list
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.reverse() # [4, 5, 2, 3, 1, 6, 5, 4, 3, 2, 1]
data == some_list # False

# sort()      Sort items in a list in ascending order
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
data.sort() # [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
data == some_list # False

data.sort(reverse=True) # [6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
data == some_list # False

# sorted()
data = some_list.copy() # [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
sorted(data) # [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
data == some_list # True
