def division_error(a, b):
    errors = {b == 0: ZeroDivisionError,
             isinstance(b, str): TypeError}
    try:
        a / b
    except errors[True] as e:
        print(e)


def raise_error(a, b):
    invalid_case = isinstance(a, str) or isinstance(b, str)
    if invalid_case:
        raise TypeError()
    a + b
