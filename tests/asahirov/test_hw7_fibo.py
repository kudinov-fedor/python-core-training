"""
Create decorator which would remember answers,
and if answer was given, do not make a call to a function
"""


def remember_answer(func):
    answer = {}
    call_count = {"count": 0}

    def remember(*args):
        try:
            hash(args)
        except Exception:
            raise TypeError("input args not hashable ")
        result = func(*args)
        if result not in answer:
            call_count["count"] += 1
            answer[result] = result
        return answer[result]

    remember.call_count = call_count
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


def test_remember_answer_decorator(mocker):
    spy = mocker.spy(fibo)
    fibo(10)
    assert spy.call_count == 10
