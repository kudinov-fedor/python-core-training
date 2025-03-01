def group_dictionary(data_input, key):
    by_res = {}
    for i in data_input:
        if i[key] not in by_res:
            by_res[i[key]] = []
        by_res[i[key]].append(i)
    return by_res
