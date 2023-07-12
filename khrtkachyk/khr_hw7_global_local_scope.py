def create_global_variable():
    global lst
    lst = [1, 2, 3, 4, 5]


def use_global_variable():
    lst.append(6)


def return_sum():
    return sum(lst)


def create_global_variable_2_0(key, value):
    globals()[key] = value


def use_global_variable_2_0(key):
    return globals()[key]


if __name__ == "__main__":
    create_global_variable()
    print(f'Created global variable: {lst}')
    print(f'Sum of list items = {return_sum()}')
    use_global_variable()
    print(f'Modified global variable: {lst}')
    print(f'Sum of list items = {return_sum()}')
    create_global_variable_2_0("age", 30)
    print(f'Getting value from created global variable: {use_global_variable_2_0("age")}')
