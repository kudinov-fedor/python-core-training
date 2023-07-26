"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""
new_dict = {}


def decorator(func):
    def inner(*args):
        if args in new_dict:
            return new_dict[args]
        else:
            result = func(*args)
            new_dict.update({args: result})
            return result
    return inner


@decorator
def fibo(n: int):
    """
    Count fibonache numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """
    if n < 3:
        return [0, 1, 2][n]
    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(fibo(i))
