def group_dictionary(data_input):
    by_sex = {}
    for i in data_input:
        if i["sex"] not in by_sex:
            by_sex[i["sex"]] = []
        by_sex[i["sex"]].append(i)
    return by_sex
