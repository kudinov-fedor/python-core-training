import pytest
from tkupchyn.homework_08.warior import (Warrior, Knight, fight)


@pytest.mark.parametrize('unit1, unit2, expected_result',
                         (
                                 (Warrior(), Warrior(), True),
                                 (Warrior(), Knight(), False),
                                 (Warrior(), Warrior(), True),
                                 (Knight(), Knight(), True),

                         ))
def test_fight(unit1, unit2, expected_result):
    assert fight(unit1, unit2) == expected_result


@pytest.mark.parametrize('unit1, unit2, expected_result',
                         (
                                 (Warrior(), Warrior(),
                                  {'before_fight': True, 'after_fight': True}),

                                 (Warrior(), Knight(),
                                  {'before_fight': True, 'after_fight': False}),

                                 (Warrior(), Warrior(),
                                  {'before_fight': True, 'after_fight': True}),

                                 (Knight(), Knight(),
                                  {'before_fight': True, 'after_fight': True})

                         ))
def test_is_alive(unit1, unit2, expected_result):
    assert unit1.is_alive == expected_result['before_fight']
    fight(unit1, unit2)
    assert unit1.is_alive == expected_result['after_fight']
