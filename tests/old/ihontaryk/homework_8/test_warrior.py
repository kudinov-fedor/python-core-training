import pytest

from ihontaryk.homework_8.warrior import Warrior, Knight, fight


@pytest.fixture(scope='module')
def players():
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    return {'chuck': chuck, 'bruce': bruce, 'carl': carl, 'dave': dave, 'mark': mark}


@pytest.mark.parametrize('p1, p2, expected_result',
                         [('chuck', 'bruce', True),
                          ('dave', 'carl', False),
                          ('carl', 'mark', False)
                          ])
def test_fight(players, p1, p2, expected_result):
    """
    verify fight function
    """

    assert fight(players[p1], players[p2]) == expected_result
