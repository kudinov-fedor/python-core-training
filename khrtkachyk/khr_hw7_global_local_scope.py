def create_global_variable():
    global lst
    lst = [1, 2, 3, 4, 5]
    return sum(lst)


def use_global_variable():
    global lst
    lst.append(6)
    return sum(lst)


def create_global_variable_2_0(key, value):
    globals()[key] = value
    return key, value


def use_global_variable_2_0(key):
    return globals()[key]


if __name__ == "__main__":
    create_global_variable()
    print(f'Created global variable: {lst}; Sum of list items = {create_global_variable()}')
    use_global_variable()
    print(f'Modified global variable: {lst}; Sum of list items when reusing global lst = {use_global_variable()}')
    print(f'Key-value pair: {create_global_variable_2_0("age", 30)}')
    print(f'Getting value from created global variable: {use_global_variable_2_0("age")}')
