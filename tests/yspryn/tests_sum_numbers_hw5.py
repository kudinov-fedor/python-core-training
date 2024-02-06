from yspryn.checkio_tasks.sum_numbers_hw5 import sum_numbers, sum_numbers2


def test_sum_numbers():
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
            sum_numbers(
                "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
            )
            == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0

def test_sum_numbers2():
    assert sum_numbers2("hi") == 0
    assert sum_numbers2("who is 1st here") == 0
    assert sum_numbers2("my numbers is 2") == 2
    assert (
            sum_numbers2(
                "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
            )
            == 3755
    )
    assert sum_numbers2("5 plus 6 is") == 11
    assert sum_numbers2("") == 0
