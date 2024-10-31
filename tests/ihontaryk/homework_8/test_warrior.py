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
                         [('chuck', 'bruce', True)])
def test_fight_first(players, p1, p2, expected_result):
    """
    verify fight function for first fight
    """

    assert fight(players[p1], players[p2]) == expected_result


@pytest.mark.parametrize('p1, p2, expected_result',
                         [('dave', 'carl', False)])
def test_fight_second(players, p1, p2, expected_result):
    """
    verify fight function for second fight
    """

    assert fight(players[p1], players[p2]) == expected_result


@pytest.mark.parametrize('p1, p2, expected_result',
                         [('carl', 'mark', False)])
def test_fight_third(players, p1, p2, expected_result):
    """
    verify fight function for third fight
    """

    assert fight(players[p1], players[p2]) == expected_result
