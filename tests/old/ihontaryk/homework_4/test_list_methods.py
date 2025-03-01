import pytest


@pytest.mark.parametrize('data1, data2, expected_result',
                         [(['beautifulwolf165', 'Kennedy', 'Debbie', 'female'],
                           [15439, 'Michigan', 'Hialeah', '5236 Sunset St', '(766)-339-9897'],
                           ['beautifulwolf165', 'Kennedy', 'Debbie', 'female', 15439, 'Michigan', 'Hialeah',
                            '5236 Sunset St', '(766)-339-9897']
                           )])
def test_extend_lists(data1, data2, expected_result):
    """
    verify extending user details by contacts
    """
    data1.extend(data2)

    assert data1 == expected_result
