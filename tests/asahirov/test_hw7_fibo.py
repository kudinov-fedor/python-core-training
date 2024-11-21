from tests.asahirov import hw7_fibo


def test_remember_answer_decorator(mocker):
    spy = mocker.spy(hw7_fibo, "fibo")
    hw7_fibo.fibo(10)
    assert spy.call_count == 17
    hw7_fibo.fibo(8)
    assert spy.call_count == 18
    hw7_fibo.fibo(12)
    assert spy.call_count == 23
