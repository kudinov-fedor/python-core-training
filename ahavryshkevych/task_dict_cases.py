def dict_comparison(dict1, dict2):
    return dict1 == dict2


def dict_compr_convert(test_dict):
    conv_dict = {k * 2: str(v) for k, v in test_dict.items()}
    result = []
    for val in conv_dict.values():
        if isinstance(val, str):
            result.append(isinstance(val, str))
    return all(result)


def dict_gender_check(dict_data):
    by_sex = {}
    for i in dict_data:
        if i["sex"] not in by_sex:
            by_sex[i["sex"]] = []
        by_sex[i["sex"]].append(i)
    return len(by_sex["M"]) > len(by_sex["F"])


def dict_value_change(dict_data, key, new_data):
    dict_data[key] = new_data
    return dict_data[key]
