import collections
from irepela.homework_9.french_deck import FrenchDeck


def test_french_deck():
    Card = collections.namedtuple('Card', ['rank', 'suit'])
    deck = FrenchDeck()

    assert len(deck) == 52
    assert deck[0] == Card(rank='2', suit='spades')
    assert deck[51] == Card(rank='A', suit='hearts')
    assert deck[:3] == [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    assert (Card('5', 'clubs') in deck) is True
    assert (Card('blablabla', 'xyz') in deck) is False

    deck[0] = deck[-1]
    assert deck[0] == Card(rank='A', suit='hearts')
