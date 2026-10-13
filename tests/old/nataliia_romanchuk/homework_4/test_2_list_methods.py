some_str = "fabcdefdgab"
some_list = [1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4]
some_tuple = (1, 2, 3, 4, 5, 6, 1, 3, 2, 5, 4)

def test_index():
    assert some_tuple.index(2)==1
    assert some_list.index(2)
    assert some_str.index("d")==4
    assert some_str.index("ab")

def test_count():
    assert some_tuple.count(3)==2
    assert some_list.count(3)==2
    assert some_str.count("a")==2
    assert some_str.count("ab")==2


# Methods Specific Only for List

# copy()      Returns a shallow copy of the list
def test_copy():
    data = some_list.copy()
    assert data == some_list
    assert id(data) != id(some_list)
    assert data is not some_list

# Next Methods change List

# append()    Adds an element at the end of the list
def test_append():
    data = some_list.copy()
    data.append(100)
    assert not data == some_list

# insert()    Adds an element at the specified position
def test_insert():
    data = some_list.copy()
    data.insert(0, "a")   # insert in front
    assert not data == some_list

    data = some_list.copy()
    data.insert(-1, "a")  # insert before last
    assert not data == some_list

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
