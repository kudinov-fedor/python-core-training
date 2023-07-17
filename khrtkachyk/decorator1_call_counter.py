"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""


def my_decor(original_func):
    cached = {}

    def wrapper(n: int):
        if n not in cached:
            res = original_func(n)
            cached[n] = res
        return cached[n]

    return wrapper


@my_decor
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
