global_var = "Global Variable"


def change_global(value):
    global global_var
    global_var = value


def get_global():
    return global_var
