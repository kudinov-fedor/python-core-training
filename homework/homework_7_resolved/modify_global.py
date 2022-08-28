some_var = None


def modify_global(value):
    global some_var
    some_var = value


def get_global():
    return some_var


if __name__ == "__main__":
    assert some_var is None
    modify_global(123)
    assert get_global() == 123
    assert some_var == 123
