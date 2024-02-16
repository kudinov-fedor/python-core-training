"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""


def remember_answer(func):
    answer = {}

    def remember(*args):
        try:
            hash(args)
        except Exception:
            raise TypeError("input args not hashable ")
        if args in answer:
            return answer[args]
        else:
            result = func(*args)
            answer[args] = result
            return result

    return remember


@remember_answer
def fibo(n: int):
    """
    Count fibonache numbers, where next is sum of 2 prior
    1, 2, 3, 5, 8, 13, 21, ...
    """
    if n < 3:
        return [0, 1, 2][n]
    return fibo(n - 1) + fibo(n - 2)
