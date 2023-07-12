def create_global_variable():
    global lst
    lst = [1, 2, 3, 4, 5]


def add_to_global_variable(item: int):
    lst.append(item)


def return_sum():
    return sum(lst)


def create_global_variable_2_0(key, value):
    globals()[key] = value


def use_global_variable_2_0(key):
    return globals()[key]
