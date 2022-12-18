import pytest

from obalk.checkio.home.bigger_price import bigger_price


@pytest.mark.parametrize("count_highest, bucket, result", [
    (
            2, [{'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15},
                {'name': 'water', 'price': 1}],
            [{'name': 'wine', 'price': 138}, {'name': 'bread', 'price': 100}]
    ),
])
def test_duplicate_zeros(count_highest, bucket, result):
    assert bigger_price(count_highest, bucket) == result
