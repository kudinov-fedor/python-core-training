from collections import defaultdict


def filter_by_property(data):
    by_sex = defaultdict(list)  # if key is not present, it will be created with value = list()
    for i in data:
        by_sex[i["sex"]].append(i)

    return len(by_sex["M"]), len(by_sex["F"])