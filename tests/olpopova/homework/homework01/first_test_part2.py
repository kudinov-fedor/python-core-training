import pytest


@pytest.mark.parametrize(['num1', 'num2', 'res'], [
    ('abc', 2, 'abcabc'),
    ((2, ), 5, (2, 2, 2, 2, 2)),
    (2, 5, 10),
    ([4, 5], 2, [4, 5, 4, 5])
])
def test_multiplicaion(num1, num2, res):
    assert num1 * num2 == res


def sum_operation(num1, num2):
    return num1 + num2


actual_list = sum_operation([4, 5], [3, 9])
result = sum(actual_list)
print(result)
