import pytest

from ihontaryk.homework_9.frenchdeck import FrenchDeck


@pytest.fixture
def deck():
    return FrenchDeck()


@pytest.mark.parametrize('index, expected_result',
                         [(1, ('3', 'spades')),
                          (slice(42, 52, 2), [('5', 'hearts'),
                                              ('7', 'hearts'),
                                              ('9', 'hearts'),
                                              ('J', 'hearts'),
                                              ('K', 'hearts'),
                                              ]),
                          (slice(3), [('2', 'spades'),
                                      ('3', 'spades'),
                                      ('4', 'spades')]),
                          ])
def test_getitem(deck, index, expected_result):
    """
    verify getitem function
    """

    assert deck[index] == expected_result


@pytest.mark.parametrize('index, new_value, expected_result',
                         [(0, ('K', 'hearts'),
                           ('K', 'hearts')),
                          (slice(1, 4), [('3', 'diamonds'),
                                         ('4', 'clubs'),
                                         ('5', 'hearts')],
                           [('3', 'diamonds'),
                            ('4', 'clubs'),
                            ('5', 'hearts')])
                          ])
def test_setitem(deck, index, new_value, expected_result):
    """
    verify setitem function
    """

    deck[index] = new_value
    assert deck[index] == expected_result
