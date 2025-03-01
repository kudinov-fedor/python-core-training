import pytest


@pytest.mark.parametrize('data1, expected_result',
                         [(
                                 [{'username': 'yellowrabbit122', 'last_name': 'Marshall', 'first_name': 'Zoey',
                                   'gender': 'female'},
                                  {'username': 'ticklishdog243', 'last_name': 'Marshall', 'first_name': 'Herman',
                                   'gender': 'male'},
                                  {'username': 'silverfrog870', 'last_name': 'Robinson', 'first_name': 'Brian',
                                   'gender': 'male'},
                                  {'username': 'heavykoala856', 'last_name': 'Andrews', 'first_name': 'Liam',
                                   'gender': 'male'},
                                  {'username': 'goldenbird473', 'last_name': 'Andrews', 'first_name': 'Jacqueline',
                                   'gender': 'female'}],
                                 [{'username': 'goldenbird473', 'last_name': 'Andrews', 'first_name': 'Jacqueline',
                                   'gender': 'female'},
                                  {'username': 'heavykoala856', 'last_name': 'Andrews', 'first_name': 'Liam',
                                   'gender': 'male'},
                                  {'username': 'ticklishdog243', 'last_name': 'Marshall', 'first_name': 'Herman',
                                   'gender': 'male'},
                                  {'username': 'yellowrabbit122', 'last_name': 'Marshall', 'first_name': 'Zoey',
                                   'gender': 'female'},
                                  {'username': 'silverfrog870', 'last_name': 'Robinson', 'first_name': 'Brian',
                                   'gender': 'male'}]
                         )])
def test_sorting_by_2_parameters(data1, expected_result):
    """
    verify sorting by last name and then first name
    """

    assert sorted(data1, key=lambda i: (i['last_name'], i['first_name'])) == expected_result
