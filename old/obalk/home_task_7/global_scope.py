def change_global(variable, value):
    variables = globals()
    if variable not in variables:
        print(f"'{variable}' is not presented in globals. Changes are not applied")
        return
    globals()[variable] = value


def get_global(variable):
    try:
        result = globals()[variable]
    except KeyError:
        print(f"'{variable}' is not presented in globals. Information wasn't gotten")
        return "Doesn't exist"
    return result


if __name__ == "__main__":
    print(globals())
    print(get_global("__name__"))
    print(get_global("__aname__"))
    print(change_global("__doc__", "Some special doc"))
    print(get_global("__doc__"))
    print(globals())
