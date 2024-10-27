import pytest
from ihontaryk.homework_8.warrior import Warrior, Knight, fight

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

@pytest.mark.parametrize('p1, p2, expected_result',
                         [(chuck, bruce, True)])

def test_fight_first(p1, p2, expected_result):
    """
    verify fight function for first fight
    """

    assert fight(p1, p2) == expected_result


@pytest.mark.parametrize('p1, p2, expected_result',
                         [(dave, carl, False)])

def test_fight_second(p1, p2, expected_result):
    """
    verify fight function for second fight
    """

    assert fight(p1, p2) == expected_result


@pytest.mark.parametrize('p1, p2, expected_result',
                         [(carl, mark, False)])

def test_fight_third(p1, p2, expected_result):
    """
    verify fight function for third fight
    """

    assert fight(p1, p2) == expected_result
