"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""


def decorator_answers(func):
    remember_result = {}

    def wrapper(n: int):
        if n not in remember_result:
            res = func(n)
            remember_result[n] = res
        else:
            return remember_result[n]
        return remember_result
    return wrapper


@decorator_answers
def fibo(n: int):
    """
    Count fibonache numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """
    if n < 3:
        return [0, 1, 2][n]
    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    for i in range(6):
        print(fibo(i))
