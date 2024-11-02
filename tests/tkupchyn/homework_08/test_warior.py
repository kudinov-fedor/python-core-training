import pytest
from tkupchyn.homework_08.warior import (Warrior, Knight, fight)


@pytest.fixture()
def duel_pairs():
    return [(Warrior(), Warrior()),
            (Warrior(), Knight()),
            (Warrior(), Warrior()),
            (Knight(), Knight())]


def test_fight(duel_pairs):
    expected_result = [True, False, True, True]
    for i in range(len(duel_pairs)):
        assert fight(duel_pairs[i][0], duel_pairs[i][1]) == expected_result[i]


def test_is_alive(duel_pairs):
    expected_result = [{'before_fight': True, 'after_fight': True},
                       {'before_fight': True, 'after_fight': False},
                       {'before_fight': True, 'after_fight': True},
                       {'before_fight': True, 'after_fight': True}]
    for i in range(len(duel_pairs)):
        assert duel_pairs[i][0].is_alive == expected_result[i]['before_fight']
        fight(duel_pairs[i][0], duel_pairs[i][1])
        assert duel_pairs[i][0].is_alive == expected_result[i]['after_fight']
