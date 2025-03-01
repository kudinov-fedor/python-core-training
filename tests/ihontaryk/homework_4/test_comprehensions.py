import pytest


@pytest.mark.parametrize('data1, expected_result',
                         [(['Edgar', 'Roger', 'Andrea', 'Arnold', 'Brayden', 'Andrea', 'Walter', 'Andrea', 'Stephen',
                            'Andrea', 'Edgar', 'Roger'],
                           ['Andrea', 'Arnold', 'Brayden', 'Edgar', 'Roger', 'Stephen', 'Walter']
                           )])
def test_sorting_unique_first_names(data1, expected_result):
    """
    verify sorting unique first name
    """

    assert sorted({i for i in data1}) == expected_result
