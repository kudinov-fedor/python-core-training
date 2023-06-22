import pytest


@pytest.mark.parametrize(['num1', 'num2', 'res'], [
    # ('abc', 2, 'abcabc'),
    # ((2, ), 5, 22222),
    (2, 5, 22222),
    ([4, 5], 2, [4, 5, 4, 5])
])
def test_multiplicaion(num1, num2, res):
    return num1 * num2


# @pytest.mark.parametrize(['num1', 'num2', 'res'], [
#     ((1, 4), (2, 6), (1, 4, 2, 6)),
#     ([4, 5], [3, 9], [4, 5, 3, 9]),
# ])
# def sum_operation(num1, num2, res):
def sum_operation(num1, num2):
    return num1 + num2
# assert num1 + num2 == res


actual_list = sum_operation([4, 5], [3, 9])
result = sum(actual_list)
print(result)
