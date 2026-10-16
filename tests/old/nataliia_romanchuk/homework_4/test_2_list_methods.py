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
    assert not data is some_list
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
def test_clear():
    data = some_list.copy()
    data.clear()
    assert not data == some_list
    assert not data

# extend()    Add the elements of a list (or any iterable), to the end of the current list
def test_extend_list():
    data = some_list.copy()
    nummm=len(data)
    data.extend([100, 200, 300])
    assert data.index(100)==nummm
    assert not data == some_list

def test_extend_str():
    data = some_list.copy()
    data.extend("abc")
    assert data.index("a")
    if "a" in some_list:
        res=some_list.index("a")
    else:
        res=None
    assert not res
    assert "a" or "b" or "c" not in some_list
    assert "a" and "b" and "c" not in some_list
    assert "a" or "b" or "c"  in data
    assert "a" and "b" and "c" in data

def test_extend_with_dict():
    data = some_list.copy()
    data.extend({"a": 123, "b": 456})
    assert "a" in data and "b" in data

# pop()       Removes and returns the element at the specified position
def test_pop():
    data = some_list.copy()
    last=data[-1]
    popped_item = data.pop()  # pop last
    assert data != some_list
    assert last == popped_item

    data = some_list.copy()
    first=data[0]
    popped_item = data.pop(0)   # pop first
    assert first == popped_item

# remove()    Removes the item with the specified value
def test_remove():
    data = some_list.copy()
    five_count = data.count(5)
    data.remove(5)  # remove first occurrence
    assert data.count(5) == five_count-1
    assert data.count(5) < five_count

# reverse()   Reverses the order of items in the list
def test_reverse():
    data = some_list.copy()
    data.reverse()
    assert data != some_list
    assert data[0]==some_list[-1]

# sort()      Sort items in a list in ascending order
def test_sort():
    data = some_list.copy()
    data.sort()
    data[0]<data[-1]
    assert all(data[i]<=data[i+1] for i in range(len(data)-1))
    assert data == sorted(some_list)

    data.sort(reverse=True)
    assert data[0]>data[-1]
