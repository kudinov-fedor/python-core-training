import pytest

from yspryn.checkio_tasks.even_the_last import even_the_last


@pytest.mark.parametrize("input_list, res", [
    ([-43, -72, 3, -83, -82, 93, -59, -80, 6, -39, 16, 39, 1, 47, -19, 67, 51], -6426),
    ([], 0),
    ([45], 2025),
    ([69, -91, -49, -29, 13, -42, 34, -99, -97, -80, 16, -9], 126),
    ([-6], 36)
])
def test_even_the_last(input_list, res):
    assert even_the_last(input_list) == res
