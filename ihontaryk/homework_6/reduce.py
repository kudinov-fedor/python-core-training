from operator import add, mul


def custom_reduce(*args, key: callable, default):
    """
    Function that returns total result
    """

    if not args:
        return default

    total, *args = args

    for arg in args:
        total = key(total, arg)

    return total


def custom_sum(*args):
    """
    Function to calculate the sum of arguments
    """

    return custom_reduce(*args, key=add, default=0)


if __name__ == "__main__":
    print(custom_reduce(-7, -4, -2, 1, 2, 3, 4, 5, 6, key=mul, default=1))
    print(custom_sum(-7, -4, -2, 1, 2, 3, 4, 5, 6))
