import pytest

from homework.homework_9.frenchdeck import FrenchDeck, Card
from random import shuffle


@pytest.mark.parametrize(['card', 'position_in_deck'], [
    (Card('A', 'hearts'), 0),
    (Card('9', 'spades'), 21),
])
def test_french_desk(card, position_in_deck):
    deck = FrenchDeck()
    assert card in deck

    card_in_deck = deck[position_in_deck]
    shuffle(deck)
    assert (deck[position_in_deck] != card_in_deck) is True
