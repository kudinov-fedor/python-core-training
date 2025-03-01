# comprehensions
from randomuser import RandomUser

some_list = [1, 2, 3, 4, 5]  # [1, 2, 3, 4, 5]
some_dict = {"a": 1, "b": 2, "c": 3}  # {'a': 1, 'b': 2, 'c': 3}

(i for i in some_list)  # generator expression: <generator object <genexpr> at 0x000001DFF11F3B80>
[i for i in some_list]  # list comprehension: [1, 2, 3, 4, 5]
{i for i in some_list}  # set comprehension: {1, 2, 3, 4, 5}
{i: i * 2 for i in some_list}  # dict comprehension: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# create generator object using generator expression
# and unpack items form it into list, set, dict, tuple
list((i for i in some_list))  # [1, 2, 3, 4, 5]
set((i for i in some_list))  # {1, 2, 3, 4, 5}
dict(((i, i * 2) for i in some_list))  # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
tuple((i for i in some_list))  # (1, 2, 3, 4, 5)

# if generator expression is 1 and only 1 parameter,
# parenthesis can be avoided
list(i for i in some_list)  # [1, 2, 3, 4, 5]
set(i for i in some_list)  # {1, 2, 3, 4, 5}
dict((i, i * 2) for i in some_list)  # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
tuple((i for i in some_list))  # (1, 2, 3, 4, 5)

# comprehensions with filtration and item modification
[i * 2 for i in some_list if i <= 3]  # [2, 4, 6]
(i * 2 for i in some_list if i <= 3)  # <generator object <genexpr> at 0x000001DFF132D560>
{i * 2 for i in some_list if i <= 3}  # {2, 4, 6}
{i: i * 2 for i in some_list if i <= 3}  # {1: 2, 2: 4, 3: 6}

# process dict in comprehensions, same as during iteration
[some_dict[k] * 2 for k in some_dict if some_dict[k] <= 2]  # [2, 4]
[k for k in some_dict if some_dict[k] <= 2]  # ['a', 'b']

[i[1] * 2 for i in some_dict.items() if i[1] <= 2]  # [2, 4]
[i[0] for i in some_dict.items() if i[1] <= 2]  # ['a', 'b']
[k for k, v in some_dict.items() if v <= 2]  # ['a', 'b']
[k for (k, v) in some_dict.items() if v <= 2]  # ['a', 'b']

{i[0]: i[1] for i in some_dict.items()}  # {'a': 1, 'b': 2, 'c': 3}
{k: v for k, v in some_dict.items()}  # {'a': 1, 'b': 2, 'c': 3}
{k: v for k, v in some_dict.items() if v <= 2}  # {'a': 1, 'b': 2}
{k * 2: v * 2 for k, v in some_dict.items() if v <= 2}  # {'aa': 2, 'bb': 4}

# collect data
data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]

ages = {i["age"] for i in data}  # {16, 25, 34}
names = {i["name"] for i in data}  # {'John', 'Marry', 'Mathew'}


def filter_unique_first_names(n):
    users = RandomUser.generate_users(n, {'nat': 'us'})

    users_list = []
    for user in users:
        users_list.append(dict(zip(['first_name'],
                                   [user.get_first_name()])))

    return sorted({i['first_name'] for i in users_list})


if __name__ == '__main__':
    print(filter_unique_first_names(10))
