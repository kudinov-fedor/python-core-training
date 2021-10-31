def nearest_value(values: set, one: int) -> list:
    nearest_value_list = list()
    for value in values:
        elem = abs(value-one)
        nearest_value_list.append(elem)
    minimal_minus = min(nearest_value_list)
    list_values = list(values)
    index_min_elem = nearest_value_list.index(minimal_minus)
    return list_values[index_min_elem]

