"""
pip install randomuser
"""

from randomuser import RandomUser


some_str = "abcd"  # 'abcd'
some_tuple = "a", "b", "c", "d"  # ('a', 'b', 'c', 'd')
some_list = ["a", "b", "c", "d"]  # ['a', 'b', 'c', 'd']
some_set = {"a", "b", "c", "d"}  # {'d', 'b', 'c', 'a'}
some_dict = {"a": 123, "b": 456, "c": 789, "d": 100}  # {'a': 123, 'b': 456, 'c': 789, 'd': 100}

# len
len(some_str)  # 4
len(some_tuple)  # 4
len(some_list)  # 4
len(some_set)  # 4
len(some_dict)  # 4

# contains
var = "a" in some_str  # True
var = "a" in some_tuple  # True
"a" in some_list  # True
"a" in some_set  # True
"a" in some_dict  # True

# getitem
some_str[0]  # 'a'
some_tuple[0]  # 'a'
some_list[0]  # 'a'
some_dict["a"]  # 123

# last item
some_str[-1]  # 'd'
some_tuple[-1]  # 'd'
some_list[-1]  # 'd'

# modify
a = [1, 2, 3, 4]  # [1, 2, 3, 4]
a[3] = "abc"  # a: [1, 2, 3, 'abc']
del a[1]  # a: [1, 3, 'abc']

b = {"a": 123, "b": 456}  # {'a': 123, 'b': 456}
b["c"] = 7889  # b: {'a': 123, 'b': 456, 'c': 7889}
b["b"] = "some"  # b: {'a': 123, 'b': 'some', 'c': 7889}
del b["a"]  # {'b': 'some', 'c': 7889}

# unpack / iterate
list(some_str)  # ['a', 'b', 'c', 'd']
list(some_tuple)  # ['a', 'b', 'c', 'd']
list(some_list)  # ['a', 'b', 'c', 'd']
list(some_set)  # ['d', 'b', 'c', 'a']
list(some_dict)  # ['a', 'b', 'c', 'd']

tuple(some_str)  # ('a', 'b', 'c', 'd')
tuple(some_tuple)  # ('a', 'b', 'c', 'd')
tuple(some_list)  # ('a', 'b', 'c', 'd')
tuple(some_set)  # ('d', 'b', 'c', 'a')
tuple(some_dict)  # ('a', 'b', 'c', 'd')

# multiple assignment
a, b, c, d = some_str  # 'abcd'
a, b, c, d = some_tuple  # ('a', 'b', 'c', 'd')
a, b, c, d = some_list  # ['a', 'b', 'c', 'd']
a, b, c, d = some_set  # {'d', 'b', 'c', 'a'}
a, b, c, d = some_dict  # {'a': 123, 'b': 456, 'c': 789, 'd': 100}

a, *tail = some_str  # tail: ['b', 'c', 'd'] - Test
a, *tail = some_tuple  # tail: ['b', 'c', 'd'] - Test
a, *tail = some_list  # tail: ['b', 'c', 'd'] - Test
a, *tail = some_set  # tail: ['b', 'c', 'a']
a, *tail = some_dict  # tail: ['b', 'c', 'd'] - Test

*head, d = some_str  # head: ['a', 'b', 'c']
*head, d = some_tuple  # head: ['a', 'b', 'c']
*head, d = some_list  # head: ['a', 'b', 'c']
*head, d = some_set  # head: ['d', 'b', 'c']
*head, d = some_dict  # head: ['a', 'b', 'c']

a, *middle, d = some_str  # middle: ['b', 'c']
a, *middle, d = some_tuple  # middle: ['b', 'c']
a, *middle, d = some_list  # middle: ['b', 'c']
a, *middle, d = some_set  # middle: ['b', 'c']
a, *middle, d = some_dict  # middle: ['b', 'c']

a, b, c, d, *tail = some_str  # []
a, b, c, d, *tail = some_tuple  # []
a, b, c, d, *tail = some_list  # []
a, b, c, d, *tail = some_set  # []
a, b, c, d, *tail = some_dict  # []

# iterate protocol
some_str_iter = iter(some_str)
next(some_str_iter)  # get 1 item from iterator
list(some_str_iter)  # get all rest items from iterator
list(some_str_iter)  # iterator exhausted, no items are returned

some_tuple_iter = iter(some_tuple)  # <str_ascii_iterator object at 0x0000022908AC08E0>
next(some_tuple_iter)  # 'a'
list(some_tuple_iter)  # ['b', 'c', 'd']
list(some_tuple_iter)  # []

some_list_iter = iter(some_list)  # <list_iterator object at 0x0000022908AC19F0>
next(some_list_iter)  # 'a'
list(some_list_iter)  # ['b', 'c', 'd']
list(some_list_iter)  # []

some_set_iter = iter(some_set)  # <set_iterator object at 0x0000022908B3B240>
next(some_set_iter)  # 'd'
list(some_set_iter)  # ['b', 'c', 'a']
list(some_set_iter)  # []

some_dict_iter = iter(some_dict)  # <dict_keyiterator object at 0x00000229088AF970>
next(some_dict_iter)  # 'a'
list(some_dict_iter)  # ['b', 'c', 'd']
list(some_dict_iter)  # []

# sort data (same for min max)
data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]

# sort by age -- Test --
sorted(data, key=lambda i: i["age"])
# [{'age': 16, 'name': 'John', 'sex': 'M'}, {'age': 25, 'name': 'Mathew', 'sex': 'M'}, {'age': 34, 'name': 'Marry', 'sex': 'F'}]
sorted(data, key=lambda i: i["age"], reverse=True)
# [{'age': 34, 'name': 'Marry', 'sex': 'F'}, {'age': 25, 'name': 'Mathew', 'sex': 'M'}, {'age': 16, 'name': 'John', 'sex': 'M'}]

# sort by sex, where F is 0, M is 1 (F goes first - ascending by default)
sorted(data, key=lambda i: i[
                               "sex"] == "M")  # [{'age': 34, 'name': 'Marry', 'sex': 'F'}, {'age': 16, 'name': 'John', 'sex': 'M'}, {'age': 25, 'name': 'Mathew', 'sex': 'M'}]
sorted(data, key=lambda i: i["sex"] == "M", reverse=True)  # [{'age': 16, 'name': 'John', 'sex': 'M'}, {'age': 25, 'name': 'Mathew', 'sex': 'M'}, {'age': 34, 'name': 'Marry', 'sex': 'F'}]

# sort by sex (F first) and age (asc)
sorted(data, key=lambda i: (i["sex"] == "M", i["age"]))  # [{'age': 34, 'name': 'Marry', 'sex': 'F'}, {'age': 16, 'name': 'John', 'sex': 'M'}, {'age': 25, 'name': 'Mathew', 'sex': 'M'}]
# sort by sex (F first) and age (desc)
sorted(data, key=lambda i: (i["sex"] == "M", -i["age"]))  # [{'age': 34, 'name': 'Marry', 'sex': 'F'}, {'age': 25, 'name': 'Mathew', 'sex': 'M'}, {'age': 16, 'name': 'John', 'sex': 'M'}]
# sort by name  alphabetically
sorted(data, key=lambda i: i["name"])  # [{'age': 16, 'name': 'John', 'sex': 'M'}, {'age': 34, 'name': 'Marry', 'sex': 'F'}, {'age': 25, 'name': 'Mathew', 'sex': 'M'}]

# zip, enumerate, reversed, map, filter --Tests--
list(filter(lambda i: i == "M", data))  # []
list(enumerate(data))  # [(0, {'age': 16, 'name': 'John', 'sex': 'M'}), (1, {'age': 34, 'name': 'Marry', 'sex': 'F'}), (2, {'age': 25, 'name': 'Mathew', 'sex': 'M'})]
list(reversed(data))  # [{'age': 25, 'name': 'Mathew', 'sex': 'M'}, {'age': 34, 'name': 'Marry', 'sex': 'F'}, {'age': 16, 'name': 'John', 'sex': 'M'}]
list(map(lambda i: i["name"], data))  # ['John', 'Marry', 'Mathew']

list(zip(data, [1, 2, 3, 4, 5, 6, 7]))  # [({'age': 16, 'name': 'John', 'sex': 'M'}, 1), ({'age': 34, 'name': 'Marry', 'sex': 'F'}, 2), ({'age': 25, 'name': 'Mathew', 'sex': 'M'}, 3)]
list(zip(data, [1, 2]))  # [({'age': 16, 'name': 'John', 'sex': 'M'}, 1), ({'age': 34, 'name': 'Marry', 'sex': 'F'}, 2)]
list(zip(data, [1, 2, 3]))  # [({'age': 16, 'name': 'John', 'sex': 'M'}, 1), ({'age': 34, 'name': 'Marry', 'sex': 'F'}, 2), ({'age': 25, 'name': 'Mathew', 'sex': 'M'}, 3)]


def sort_users_by_2_parameters(n):
    users = RandomUser.generate_users(n, {'nat': 'us'})

    users_list = []
    for user in users:
        users_list.append(dict(zip(
            ['username', 'last_name', 'first_name', 'gender'],
            [user.get_username(), user.get_last_name(), user.get_first_name(), user.get_gender()])))

    return sorted(users_list, key=lambda i: (i['last_name'], i['first_name']))


if __name__ == '__main__':
    print(sort_users_by_2_parameters(5))
