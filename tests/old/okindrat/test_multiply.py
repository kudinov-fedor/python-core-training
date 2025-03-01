# Write a function that will receive 2 numbers as input and it should return
# the multiplication of these 2 numbers.


def mult_two(a: int, b: int) -> int:
    return a * b


def test_mult():

    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0
