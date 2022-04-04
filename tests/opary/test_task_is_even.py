from opary.task_is_even import is_even


def test_is_even():
    assert is_even(270) == True
    assert is_even(39) == False
    assert is_even(1234567890) == True
    assert is_even(35792) == True
    assert is_even(0) == True
    assert is_even(-572) != False
