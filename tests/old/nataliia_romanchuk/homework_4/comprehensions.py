# comprehensions
some_list = [1, 2, 3, 4, 5]
some_dict = {"a": 1, "b": 2, "c": 3}


(i for i in some_list)  # generator expression
[i for i in some_list]  # list comprehension
{i for i in some_list}  # set comprehension
{i: i * 2 for i in some_list}  # dict comprehension

# create generator object using generator expression
# and unpack items form it into list, set, dict, tuple
list((i for i in some_list))
set((i for i in some_list))
dict(((i, i * 2) for i in some_list))
tuple((i for i in some_list))

# if generator expression is 1 and only 1 parameter,
# parenthesis can be avoided
list(i for i in some_list)
set(i for i in some_list)
dict((i, i * 2) for i in some_list)
tuple((i for i in some_list))

# comprehensions with filtration and item modification
[i * 2 for i in some_list if i <= 3]
(i * 2 for i in some_list if i <= 3)
{i * 2 for i in some_list if i <= 3}
{i: i * 2 for i in some_list if i <= 3}

# process dict in comprehensions, same as during iteration
[some_dict[k] * 2 for k in some_dict if some_dict[k] <= 2]
[k for k in some_dict if some_dict[k] <= 2]

[i[1] * 2 for i in some_dict.items() if i[1] <= 2]
[i[0] for i in some_dict.items() if i[1] <= 2]
[k for k, v in some_dict.items() if v <= 2]
[k for (k, v) in some_dict.items() if v <= 2]

{i[0]: i[1] for i in some_dict.items()}
{k: v for k, v in some_dict.items()}
{k: v for k, v in some_dict.items() if v <= 2}
{k * 2: v * 2 for k, v in some_dict.items() if v <= 2}


# collect data
data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]

ages = {i["age"] for i in data}
names = {i["name"] for i in data}
