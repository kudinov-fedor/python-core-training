def nearest_value(values: set, one: int) -> list:
    nearest_value_list = [abs(value - one) for value in values]
    index_min_elem = nearest_value_list.index(min(nearest_value_list))
    list_values = list(values)
    return list_values[index_min_elem]
