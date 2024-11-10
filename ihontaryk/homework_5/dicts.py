from collections import defaultdict

# DICTS
some_dict = {"a": 123, "b": 456, "c": 789}
some_dict_2 = {"c": 789, "a": 123, "b": 456}
some_dict_3 = dict.fromkeys("abc")  # {'a': None, 'b': None, 'c': None}
wierd_dict = {"a": 1, 2: "b",
              None: "abc",
              (1, "a"): "some",
              True: "kek",
              frozenset((1, 2)): "lol"}

some_dict == some_dict_2  # True

# is container
"a" in some_dict  # True
len(some_dict)  # 3
list(some_dict_2)  # ['c', 'a', 'b']

# methods
some_dict["a"]  # 123
some_dict.get("a")  # 123
some_dict.get("invalid", "default_val")  # 'default_val'

some = {"a": 1, "b": 2}
some.update({"b": "b", "c": "c"})
copy_of_some = some.copy()  # shallow copy
copy_of_some.clear()
item = some.pop("a")  # {'b': 'b', 'c': 'c'}
item = some.pop("invalid", "default_val")

# setdefault - return value for key, but if key not present, create it with default value, and return value
# same as:   item = data.get("k", "val")]; data["k"] = item
item = some.setdefault("a", "default_for_a")
"a" in some  # True
some["a"] == "default_for_a"  # True

item = some.setdefault("a", "other_default_for_a")
"a" in some
some["a"] == "default_for_a"

# dict comprehension
{k: v for k, v in some_dict.items()}
{k * 2: str(v) for k, v in some_dict.items()}
{k: v for k, v in some_dict.items() if k <= "b"}

# index and group
t_shirts = [{'size': 'S', 'color': 'blue', 'price': 100},
            {'size': 'M', 'color': 'black', 'price': 200},
            {'size': 'L', 'color': 'red', 'price': 300},
            {'size': 'L', 'color': 'blue', 'price': 500},
            {'size': 'M', 'color': 'pink', 'price': 550},
            {'size': 'L', 'color': 'blue', 'price': 600}, ]

dresses = [{'size': 'S', 'color': 'white', 'price': 400},
           {'size': 'M', 'color': 'pink', 'price': 500},
           {'size': 'M', 'color': 'pink', 'price': 700},
           {'size': 'L', 'color': 'yellow', 'price': 600}]

skirts = [{'size': 'S', 'color': 'black', 'price': 300},
          {'size': 'M', 'color': 'blue', 'price': 600},
          {'size': 'M', 'color': 'pink', 'price': 500},
          {'size': 'L', 'color': 'red', 'price': 400}]

clothes_shop = [{'name': 'T-shirts', 'availability': t_shirts},
                {'name': 'Dresses', 'availability': dresses},
                {'name': 'Skirts', 'availability': skirts}]


def group_by_size(clothes_shop):
    by_size = {}

    for clothes in clothes_shop:
        for item in clothes['availability']:
            if item['size'] not in by_size:
                by_size[item['size']] = []
            by_size[item['size']].append(item)

    return dict((size, len(by_size[size])) for size in by_size.keys())


# other option - setdefault:
# if key is not present, it will be created with default, and returned
def group_by_color(clothes_shop):
    by_color = {}

    for clothes in clothes_shop:
        for item in clothes['availability']:
            by_color.setdefault(item['color'], []).append(item)

    return dict((color, len(by_color[color])) for color in by_color.keys())


# Other option - use default dict
def group_by_price(clothes_shop):
    by_price = defaultdict(list)  # if key is not present, it will be created with value = list()

    for clothes in clothes_shop:
        for item in clothes['availability']:
            by_price[item['price']].append(item)

    return dict((price, len(by_price[price])) for price in by_price.keys())


def select_by_name_and_color(clothes_shop, name, color):
    selected_by_name = tuple(filter(lambda clothes:
                                    (clothes['name'] == name), clothes_shop))
    return tuple(filter(lambda item: (item['color'] == color), selected_by_name[0]['availability']))


def group_by_size_and_color(clothes_shop):
    by_size_color = defaultdict(list)

    for clothes in clothes_shop:
        for item in clothes['availability']:
            by_size_color[(item['size'], item['color'])].append(item)

    return dict((i, len(by_size_color[i])) for i in by_size_color.keys())


if __name__ == '__main__':
    print(group_by_size(clothes_shop))
    print(group_by_color(clothes_shop))
    print(group_by_price(clothes_shop))

    try:
        print(group_by_size_and_color(clothes_shop)[('M', 'pink')])
    except KeyError as e:
        print(e)
